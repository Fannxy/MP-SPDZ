#!/usr/bin/env python3
"""Generate nfgen downgrade variants for func*_kan_model_spdz.py models.

This script rewrites every neuron implementation to match the simplified
nfgen-friendly evaluation logic described in the downgrade spec. The generated
files live next to the originals using the nfgen_ prefix.
"""

from __future__ import annotations

import re
import textwrap
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
SOURCE_PATTERN = "func*_kan_model_spdz.py"
TARGET_PREFIX = "nfgen_"

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

        pre_muls = floatingpoint.PreOpL(lambda a, b, _: a * b, [x] * degree)

        poss_res = [0] * m
        for i in range(m):
            poss_res[i] = coeffA[i][0] * scaler[i][0]
            for j in range(degree):
                poss_res[i] += coeffA[i][j + 1] * pre_muls[j] * scaler[i][j + 1]

        comp = sfix.Array(m)
        for i in range(m):
            comp[i] = x >= breaks[i]

        cipher_index = Array(m, sfix)
        @for_range_opt(m - 1)
        def _(i):
            cipher_index[i] = comp[i + regint(1)]
            cipher_index[i] = comp[i] * (comp[i] - cipher_index[i])

        cipher_index[m - 1] = comp[m - 1]

        return sfix.dot_product(cipher_index, poss_res)
        """
    ),
    "    ",
)


def ensure_type_imports(content: str) -> str:
    """Ensure Array/regint are imported alongside floatingpoint/sfix."""
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
    """Add for_range_opt import when missing."""
    needle = "from Compiler.library import for_range_opt"
    if needle in content:
        return content

    anchor = "from Compiler import types\n"
    idx = content.find(anchor)
    if idx == -1:
        raise ValueError("Unable to find 'from Compiler import types' line")

    insert_at = idx + len(anchor)
    return content[:insert_at] + needle + "\n" + content[insert_at:]


def rewrite_body(content: str) -> str:
    """Replace the polynomial evaluation block with the nfgen variant."""
    replaced, count = BLOCK_PATTERN.subn(NFGEN_BLOCK, content)
    if count == 0:
        raise ValueError("Failed to replace evaluation block")
    return replaced


def transform_source(source: Path) -> str:
    content = source.read_text()
    content = ensure_type_imports(content)
    content = ensure_library_import(content)
    content = rewrite_body(content)
    return content


def main() -> None:
    for source in sorted(THIS_DIR.glob(SOURCE_PATTERN)):
        name = source.name
        if name.startswith(TARGET_PREFIX) or name.startswith("secure_"):
            continue
        nfgen_path = source.with_name(f"{TARGET_PREFIX}{name}")
        transformed = transform_source(source)
        nfgen_path.write_text(transformed)
        print(f"Wrote {nfgen_path.relative_to(THIS_DIR)}")


if __name__ == "__main__":
    main()
