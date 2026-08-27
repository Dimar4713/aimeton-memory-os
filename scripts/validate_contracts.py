#!/usr/bin/env python3
"""Validate dependency-free AMOS repository contracts.

SPDX-License-Identifier: Apache-2.0
Copyright (c) 2026 AIMETON Project
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def _load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"JSON root must be an object: {path.relative_to(ROOT)}")
    return data


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_repository_contracts() -> list[str]:
    failures: list[str] = []

    json_files = sorted(ROOT.glob("*.json")) + sorted((ROOT / "schemas").glob("*.json"))
    payloads: dict[Path, dict] = {}
    for path in json_files:
        try:
            payloads[path] = _load_json(path)
            print(f"OK  json:{path.relative_to(ROOT)}")
        except ValueError as exc:
            failures.append(str(exc))

    if failures:
        return failures

    manifest = payloads[ROOT / "manifest.json"]
    versions = payloads[ROOT / "versions.json"]
    schema_path = ROOT / "schemas" / "aimeton-cogops-coordination-snapshot.v0.2.schema.json"
    schema = payloads[schema_path]
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    checks = [
        (manifest.get("schema_version") == "1.0", "manifest.schema_version must be 1.0"),
        (manifest.get("repository") == "Dimar4713/aimeton-memory-os", "manifest.repository drifted"),
        (manifest.get("product") == "AIMETON Cognitive Operations Complex", "manifest.product drifted"),
        (manifest.get("namespace") == "AIMETON.COGOPS", "manifest.namespace drifted"),
        (manifest.get("license") == "Apache-2.0", "manifest.license drifted"),
        (len(manifest.get("authoritative_interfaces") or []) >= 6, "manifest authoritative interfaces incomplete"),
        (versions.get("repository") == "aimeton-memory-os", "versions.repository drifted"),
        (versions.get("architecture_baseline") == "AMOS external audit package v0.3", "architecture baseline drifted"),
        (versions.get("compatibility_contract") == "v0.3", "compatibility contract drifted"),
        (versions.get("coordination_snapshot_schema") == "v0.2", "coordination snapshot version drifted"),
        (pyproject.get("project", {}).get("name") == "aimeton-memory-os", "pyproject project.name drifted"),
        (pyproject.get("project", {}).get("requires-python") == ">=3.12", "Python floor must remain >=3.12"),
        (pyproject.get("project", {}).get("license", {}).get("text") == "Apache-2.0", "pyproject license drifted"),
        (schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", "coordination schema draft drifted"),
        (schema.get("additionalProperties") is False, "coordination snapshot must fail closed on unknown top-level fields"),
        (set(schema.get("required") or []) == {
            "snapshot_id",
            "axis_registry_version",
            "compatibility_registry_version",
            "axes",
            "checks",
            "outcome",
            "observed_at",
            "policy_version",
        }, "coordination snapshot required fields drifted"),
        (schema.get("properties", {}).get("axes", {}).get("minItems") == 4, "coordination snapshot must require four axes"),
        (schema.get("properties", {}).get("axes", {}).get("maxItems") == 4, "coordination snapshot must allow exactly four axes"),
        (set(schema.get("$defs", {}).get("axis", {}).get("properties", {}).get("axis_id", {}).get("enum") or []) == {"V", "R", "O", "A"}, "four-axis registry drifted"),
    ]
    for condition, message in checks:
        try:
            _require(condition, message)
        except ValueError as exc:
            failures.append(str(exc))

    sys.path.insert(0, str(SRC))
    try:
        import aimeton_memory_os  # type: ignore

        package_version = aimeton_memory_os.__version__
    except Exception as exc:  # pragma: no cover - surfaced as contract failure
        failures.append(f"package import failed: {type(exc).__name__}: {exc}")
    else:
        expected_version = str(versions.get("version"))
        project_version = str(pyproject.get("project", {}).get("version"))
        if package_version != expected_version or project_version != expected_version:
            failures.append(
                "version drift: "
                f"package={package_version!r} pyproject={project_version!r} versions.json={expected_version!r}"
            )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "SPDX-License-Identifier: Apache-2.0" not in readme:
        failures.append("README SPDX identifier missing")

    if not failures:
        print("AMOS repository contracts: OK")
    return failures


def main() -> int:
    failures = validate_repository_contracts()
    if failures:
        for failure in failures:
            print(f"ERROR {failure}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
