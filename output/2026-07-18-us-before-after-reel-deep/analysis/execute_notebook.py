#!/usr/bin/env python3
"""Execute code cells from the paired notebook in one shared namespace.

This standard-library runner is used because the workspace Python does not ship
nbformat/nbconvert. It fails on the first code-cell exception and never rewrites
the source notebook.
"""

from __future__ import annotations

import json
from pathlib import Path


NOTEBOOK = Path(__file__).with_name("before_after_deep_analysis.ipynb")


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    namespace = {"__name__": "__notebook__"}
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    for index, cell in enumerate(code_cells, 1):
        source = "".join(cell["source"])
        print(f"RUN cell {index}/{len(code_cells)}")
        exec(compile(source, f"{NOTEBOOK.name}:cell-{index}", "exec"), namespace)
    print(f"PASS {len(code_cells)} code cells")


if __name__ == "__main__":
    main()
