#!/usr/bin/env python3
"""Generate secure_func*_kan_model_spdz.py variants with padded sfix parameters.

For every base func*_kan_model_spdz.py model we:
  * replace neuron evaluation logic with the simplified secure-friendly block
  * pad breaks/coeffA/scaler up to the maximum shape observed across all models,
    using -999/1.0 fillers so every neuron shares the same dimensions
  * wrap every literal in sfix(...) so the data stay secret in compiled code
"""

from __future__ import annotations

import ast
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

THIS_DIR = Path(__file__).resolve().parent
SOURCE_PATTERN = "func*_kan_model_spdz.py"
TARGET_PREFIX = "secure2_"

BLOCK_PATTERN = re.compile(
    r"[ \t]*m = len\(coeffA\).*?return sfix\.dot_product\(cipher_index, poss_res\)",
    flags=re.DOTALL,
)

NFGEN_BLOCK = textwrap.indent(
    textwrap.dedent(
        """\
        m = len(coeffA)
        k = len(coeffA[0])
        degree = k - 1
        
        comp = [x >= breaks[i] for i in range(m)]
        cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

        # pre_muls[j] 对应 x^(j+1)
        pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)
        
        col_c0 = [coeffA[i][0] for i in range(m)]
        col_s0 = [scaler[i][0] for i in range(m)]
        
        # 使用 dot_product 选出当前区间对应的 c 和 s
        # 此时 selected_c0 和 selected_s0 变成了 sfix (Secret)
        selected_c0 = sfix.dot_product(cipher_index, col_c0)
        selected_s0 = sfix.dot_product(cipher_index, col_s0)
        
        # 计算常数项结果
        final_res = selected_c0 * selected_s0

        # 4. 处理高阶项 (x^1 到 x^degree)
        for j in range(degree):
            # 提取第 j+1 列 (对应 x^(j+1))
            col_c = [coeffA[i][j+1] for i in range(m)]
            col_s = [scaler[i][j+1] for i in range(m)]
            
            # 选出当前区间的 c 和 s
            selected_c = sfix.dot_product(cipher_index, col_c)
            selected_s = sfix.dot_product(cipher_index, col_s)

            
            term = selected_c * pre_muls[j] * selected_s
            final_res += term

        return final_res
        """
    ),
    "    ",
)

# NFGEN_BLOCK = textwrap.indent(
#     textwrap.dedent(
#         """\
#         m = len(coeffA)
#         k = len(coeffA[0])
#         degree = k-1
        
#         pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

#         poss_res = [0]*m
#         for i in range(m):
#             poss_res0 = coeffA[i][0] * scaler[i][0]
#             for j in range(degree):
#                 tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
#                 poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
#             poss_res[i].reduce_after_mul()
#             poss_res[i] += poss_res0

#         comp = [x >= breaks[i] for i in range(m)]
#         cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]

#         return sfix.dot_product(cipher_index, poss_res)
#         """
#     ),
#     "    ",
# )


@dataclass(frozen=True)
class NeuronSpec:
    name: str
    breaks: List[float]
    coeffA: List[List[float]]
    scaler: List[List[float]]


@dataclass
class ModelData:
    dims: Tuple[int, int]
    neurons: Dict[str, NeuronSpec]


@dataclass
class GlobalStats:
    segments: int = 0
    cols: int = 0


def collect_models() -> Tuple[Dict[Path, ModelData], GlobalStats]:
    """Parse all base models and gather shape statistics."""
    models: Dict[Path, ModelData] = {}
    stats = GlobalStats()

    for source in sorted(THIS_DIR.glob(SOURCE_PATTERN)):
        name = source.name
        if name.startswith(TARGET_PREFIX) or name.startswith("nfgen_"):
            continue

        content = source.read_text()
        tree = ast.parse(content)

        dim_list: List[Tuple[int, int]] | None = None
        neurons: Dict[str, NeuronSpec] = {}

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                if node.name.startswith("neuron"):
                    neuron_data = extract_neuron(node)
                    neurons[node.name] = neuron_data
                elif node.name.endswith("evaluate_vectorized") and dim_list is None:
                    dim_list = extract_dim_list(node)

        if dim_list is None:
            raise ValueError(f"{source.name}: missing dim_list")

        input_dim = dim_list[0][0]
        output_dim = dim_list[-1][1]
        models[source] = ModelData(dims=(input_dim, output_dim), neurons=neurons)

        for spec in neurons.values():
            segments = len(spec.coeffA)
            cols = len(spec.coeffA[0]) if spec.coeffA else 0
            if segments > stats.segments:
                stats.segments = segments
            if cols > stats.cols:
                stats.cols = cols

    return models, stats


def extract_neuron(node: ast.FunctionDef) -> NeuronSpec:
    data: Dict[str, List] = {}
    for stmt in node.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            name = stmt.targets[0].id
            if name in {"breaks", "coeffA", "scaler"}:
                data[name] = ast.literal_eval(stmt.value)
        if len(data) == 3:
            break

    missing = {"breaks", "coeffA", "scaler"} - data.keys()
    if missing:
        raise ValueError(f"{node.name}: missing assignments for {missing}")

    def ensure_matrix(value: List) -> List[List[float]]:
        if not value:
            return []
        first = value[0]
        if isinstance(first, (int, float)):
            return [list(value)]
        return [list(row) for row in value]

    return NeuronSpec(
        name=node.name,
        breaks=list(data["breaks"]),
        coeffA=ensure_matrix(data["coeffA"]),
        scaler=ensure_matrix(data["scaler"]),
    )


def extract_dim_list(node: ast.FunctionDef) -> List[Tuple[int, int]]:
    for stmt in node.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            if stmt.targets[0].id == "dim_list":
                return list(map(tuple, ast.literal_eval(stmt.value)))
    raise ValueError("dim_list assignment not found")


def ensure_type_imports(content: str) -> str:
    pattern = re.compile(r"^from Compiler\.types import ([^\n]+)$", flags=re.MULTILINE)
    match = pattern.search(content)
    if not match:
        raise ValueError("Unable to locate 'from Compiler.types import ...' line")

    existing = {name.strip() for name in match.group(1).split(",")}
    required = ["Array", "floatingpoint", "regint", "sfix"]

    existing.update(required)
    ordered = [name for name in required if name in existing]
    remaining = sorted(existing.difference(ordered))
    updated = ordered + remaining

    new_line = f"from Compiler.types import {', '.join(updated)}"
    return content[: match.start()] + new_line + content[match.end() :]


def ensure_library_import(content: str) -> str:
    needle = "from Compiler.library import for_range_opt"
    if needle in content:
        return content

    anchor = "from Compiler import types\n"
    idx = content.find(anchor)
    if idx == -1:
        raise ValueError("Unable to find 'from Compiler import types' line")

    insert_at = idx + len(anchor)
    return content[:insert_at] + needle + "\n" + content[insert_at:]


def compute_line_offsets(content: str) -> List[int]:
    offsets: List[int] = []
    cursor = 0
    for line in content.splitlines(keepends=True):
        offsets.append(cursor)
        cursor += len(line)
    return offsets


def locate_assignments(content: str, neuron_names: Iterable[str]) -> Dict[str, Dict[str, Tuple[int, int, str, bool]]]:
    tree = ast.parse(content)
    offsets = compute_line_offsets(content)
    targets = set(neuron_names)
    result: Dict[str, Dict[str, Tuple[int, int, str, bool]]] = {}

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in targets:
            assignments: Dict[str, Tuple[int, int, str, bool]] = {}
            for stmt in node.body:
                if (
                    isinstance(stmt, ast.Assign)
                    and len(stmt.targets) == 1
                    and isinstance(stmt.targets[0], ast.Name)
                    and stmt.targets[0].id in {"breaks", "coeffA", "scaler"}
                ):
                    start = offsets[stmt.lineno - 1] + stmt.col_offset
                    end = offsets[stmt.end_lineno - 1] + stmt.end_col_offset
                    indent = " " * stmt.col_offset
                    segment = content[start:end]
                    assignments[stmt.targets[0].id] = (start, end, indent, segment.endswith("\n"))
            if assignments:
                result[node.name] = assignments
    return result


def pad_neuron(spec: NeuronSpec, global_stats: GlobalStats) -> Tuple[List[float], List[List[float]], List[List[float]]]:
    breaks = list(spec.breaks)
    coeffA = [list(row) for row in spec.coeffA]
    scaler = [list(row) for row in spec.scaler]

    target_segments = global_stats.segments
    target_cols = global_stats.cols

    if target_cols == 0:
        target_cols = len(coeffA[0]) if coeffA else 0

    # Pad existing rows to the required polynomial degree.
    for row in coeffA:
        deficit = target_cols - len(row)
        if deficit > 0:
            row.extend([1.0] * deficit)
    for row in scaler:
        deficit = target_cols - len(row)
        if deficit > 0:
            row.extend([1.0] * deficit)

    # Align the number of segments with leading fillers.
    while len(breaks) < target_segments:
        breaks.insert(0, -999.0)
        coeffA.insert(0, [1.0] * target_cols)
        scaler.insert(0, [1.0] * target_cols)

    while len(coeffA) < target_segments:
        coeffA.insert(0, [1.0] * target_cols)
        scaler.insert(0, [1.0] * target_cols)
        breaks.insert(0, -999.0)

    return breaks, coeffA, scaler


def format_number(value: float) -> str:
    return repr(value)


def format_sfix(value: float) -> str:
    return f"sfix({format_number(value)})"


def format_vector(name: str, indent: str, values: List[float]) -> str:
    indent = "    "
    inner = indent + "    "
    body = ",\n".join(f"{inner}{format_sfix(v)}" for v in values)
    return f"{indent}{name} = [\n{body}\n{indent}]"


def format_matrix(name: str, indent: str, matrix: List[List[float]]) -> str:
    indent = "    "
    inner = indent + "    "
    row_lines = []
    for row in matrix:
        row_values = ", ".join(format_sfix(v) for v in row)
        row_lines.append(f"{inner}[{row_values}]")
    body = ",\n".join(row_lines)
    return f"{indent}{name} = [\n{body}\n{indent}]"


def normalize_indent(indent: str) -> str:
    if not indent:
        return ""
    if indent.strip():
        return indent
    return " " * min(len(indent), 4)


def transform_model(source: Path, model: ModelData, stats: GlobalStats) -> str:
    content = source.read_text()
    content = ensure_type_imports(content)
    content = ensure_library_import(content)
    content = BLOCK_PATTERN.sub(NFGEN_BLOCK, content)

    assignments = locate_assignments(content, model.neurons.keys())
    replacements: List[Tuple[int, int, str]] = []

    for neuron_name, spec in model.neurons.items():
        padded_breaks, padded_coeffA, padded_scaler = pad_neuron(spec, stats)

        neuron_assigns = assignments.get(neuron_name)
        if neuron_assigns is None or len(neuron_assigns) != 3:
            raise ValueError(f"{source.name}: unable to locate assignments for {neuron_name}")

        for var_name, formatter, data in (
            ("breaks", format_vector, padded_breaks),
            ("coeffA", format_matrix, padded_coeffA),
            ("scaler", format_matrix, padded_scaler),
        ):
            start, end, indent, has_newline = neuron_assigns[var_name]
            replacement = formatter(var_name, normalize_indent(indent), data)
            if has_newline:
                replacement += "\n"
            replacements.append((start, end, replacement))

    for start, end, replacement in sorted(replacements, key=lambda item: item[0], reverse=True):
        content = content[:start] + replacement + content[end:]

    pattern = re.compile(r"\n[ \t]+((?:breaks|coeffA|scaler) = \[)")
    content = pattern.sub(lambda m: "\n    " + m.group(1), content)

    return content


def main() -> None:
    models, stats = collect_models()

    for source, model in models.items():
        secure_path = source.with_name(f"{TARGET_PREFIX}{source.name}")
        transformed = transform_model(source, model, stats)
        secure_path.write_text(transformed)
        print(f"Wrote {secure_path.relative_to(THIS_DIR)}")


if __name__ == "__main__":
    main()
