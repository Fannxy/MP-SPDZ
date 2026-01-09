#!/usr/bin/env python3
"""Report shape statistics for base and secure KAN model files."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Tuple


THIS_DIR = Path(__file__).resolve().parent
BASE_PATTERN = "func*_kan_model_spdz.py"
SECURE_PREFIX = "secure_"
NFGEN_PREFIX = "nfgen_"


@dataclass
class ModelStats:
    file: Path
    input_dim: int
    output_dim: int
    max_breaks: int
    max_coeff_rows: int
    max_coeff_cols: int
    max_scaler_rows: int
    max_scaler_cols: int


def list_length(node: ast.AST) -> int:
    if isinstance(node, ast.List):
        return len(node.elts)
    return 0


def matrix_shape(node: ast.AST) -> Tuple[int, int]:
    if not isinstance(node, ast.List):
        return 0, 0
    if not node.elts:
        return 0, 0
    first = node.elts[0]
    if isinstance(first, ast.List):
        rows = len(node.elts)
        cols = max(len(row.elts) for row in node.elts if isinstance(row, ast.List))
        return rows, cols
    return 1, len(node.elts)


def extract_dim_list(func: ast.FunctionDef) -> Tuple[int, int]:
    for stmt in func.body:
        if (
            isinstance(stmt, ast.Assign)
            and len(stmt.targets) == 1
            and isinstance(stmt.targets[0], ast.Name)
            and stmt.targets[0].id == "dim_list"
        ):
            dims = ast.literal_eval(stmt.value)
            if not dims:
                return 0, 0
            return dims[0][0], dims[-1][1]
    raise ValueError(f"{func.name}: dim_list assignment not found")


def collect_neuron_assigns(func: ast.FunctionDef) -> Dict[str, ast.AST]:
    assigns: Dict[str, ast.AST] = {}
    for stmt in func.body:
        if (
            isinstance(stmt, ast.Assign)
            and len(stmt.targets) == 1
            and isinstance(stmt.targets[0], ast.Name)
        ):
            name = stmt.targets[0].id
            if name in {"breaks", "coeffA", "scaler"}:
                assigns[name] = stmt.value
    return assigns


def analyze_file(path: Path) -> ModelStats:
    content = path.read_text()
    tree = ast.parse(content)

    input_dim = 0
    output_dim = 0
    max_breaks = 0
    max_coeff_rows = 0
    max_coeff_cols = 0
    max_scaler_rows = 0
    max_scaler_cols = 0

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if node.name.endswith("evaluate_vectorized") and input_dim == 0 and output_dim == 0:
                input_dim, output_dim = extract_dim_list(node)
            elif node.name.startswith("neuron"):
                assigns = collect_neuron_assigns(node)
                if "breaks" in assigns:
                    max_breaks = max(max_breaks, list_length(assigns["breaks"]))
                if "coeffA" in assigns:
                    rows, cols = matrix_shape(assigns["coeffA"])
                    max_coeff_rows = max(max_coeff_rows, rows)
                    max_coeff_cols = max(max_coeff_cols, cols)
                if "scaler" in assigns:
                    rows, cols = matrix_shape(assigns["scaler"])
                    max_scaler_rows = max(max_scaler_rows, rows)
                    max_scaler_cols = max(max_scaler_cols, cols)

    return ModelStats(
        file=path,
        input_dim=input_dim,
        output_dim=output_dim,
        max_breaks=max_breaks,
        max_coeff_rows=max_coeff_rows,
        max_coeff_cols=max_coeff_cols,
        max_scaler_rows=max_scaler_rows,
        max_scaler_cols=max_scaler_cols,
    )


def walk_files(pattern: str, *, include_secure: bool) -> Iterable[Path]:
    for path in sorted(THIS_DIR.glob(pattern)):
        name = path.name
        if name.startswith(NFGEN_PREFIX):
            continue
        if include_secure:
            if not name.startswith(SECURE_PREFIX):
                continue
        else:
            if name.startswith(SECURE_PREFIX):
                continue
        yield path


def format_stats(label: str, stats: Iterable[ModelStats]) -> None:
    print(label)
    for stat in stats:
        rel = stat.file.name
        print(
            f"  {rel}: in={stat.input_dim}, out={stat.output_dim}, "
            f"breaks={stat.max_breaks}, coeffA={stat.max_coeff_rows}x{stat.max_coeff_cols}, "
            f"scaler={stat.max_scaler_rows}x{stat.max_scaler_cols}"
        )
    print()


def main() -> None:
    base_stats = [analyze_file(path) for path in walk_files(BASE_PATTERN, include_secure=False)]
    secure_stats = [analyze_file(path) for path in walk_files(f"{SECURE_PREFIX}{BASE_PATTERN}", include_secure=True)]

    format_stats("Base models:", base_stats)
    format_stats("Secure models:", secure_stats)


if __name__ == "__main__":
    main()
