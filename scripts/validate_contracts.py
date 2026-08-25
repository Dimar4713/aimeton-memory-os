#!/usr/bin/env python3
"""Validate JSON contract syntax without external dependencies."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    failures = []
    for path in sorted((root / "schemas").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            print(f"OK  {path.relative_to(root)}")
        except json.JSONDecodeError as exc:
            failures.append(f"{path}: {exc}")
    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    main()
