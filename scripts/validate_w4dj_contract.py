#!/usr/bin/env python3
"""Validate the W4DJ handoff schema, fixtures, and documented Skill contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "references" / "w4dj.schema.json"
FIXTURES = ROOT / "evals" / "w4dj-fixtures.json"


def type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return False


def resolve_ref(root_schema: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/$defs/"):
        raise ValueError(f"unsupported schema reference: {reference}")
    name = reference.removeprefix("#/$defs/")
    return root_schema["$defs"][name]


def validate(
    value: Any,
    schema: dict[str, Any],
    path: str = "$",
    root_schema: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []

    root_schema = root_schema or schema
    if "$ref" in schema:
        return validate(value, resolve_ref(root_schema, schema["$ref"]), path, root_schema)

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}")
        return errors

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']!r}")
        return errors

    if "oneOf" in schema:
        branches = [validate(value, branch, path, root_schema) for branch in schema["oneOf"]]
        if sum(not branch for branch in branches) != 1:
            errors.append(f"{path}: did not match exactly one schema branch")
        return errors

    expected_types = schema.get("type")
    if expected_types is not None:
        if isinstance(expected_types, str):
            expected_types = [expected_types]
        if not any(type_matches(value, expected) for expected in expected_types):
            errors.append(f"{path}: expected type {expected_types!r}")
            return errors

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get("minimum", value):
            errors.append(f"{path}: number is below minimum")

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: array has fewer than minItems")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(validate(item, item_schema, f"{path}[{index}]", root_schema))

    if isinstance(value, dict):
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{path}: missing required property {required!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extras = sorted(set(value) - set(properties))
            errors.extend(f"{path}: unexpected property {key!r}" for key in extras)
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(validate(value[key], child_schema, f"{path}.{key}", root_schema))

    return errors


def source_contract_errors() -> list[str]:
    source_paths = (
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "references" / "export.md",
        ROOT / "references" / "report-template.md",
    )
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    required = (
        "导出w4dj",
        ".w4dj",
        "UTF-8 JSON",
        "w4dj.schema.json",
        "output_mode",
        "platform_refs",
        "dedupe_key",
        "expected_filename_hint",
        "未知",
        "不生成占位音频",
        "不处理本地音频",
    )
    errors = [f"source contract missing {fragment!r}" for fragment in required if fragment not in source]

    chinese_template_paths = (
        ROOT / "SKILL.md",
        ROOT / "references" / "report-template.md",
    )
    for path in chinese_template_paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        export_lines = [line for line in lines if "导出txt" in line]
        if not any("导出w4dj" in line for line in export_lines):
            errors.append(f"{path.name}: W4DJ must share the TXT export sentence")
        if any("您可以把本次推荐交接给 W4DJ" in line for line in lines):
            errors.append(f"{path.name}: W4DJ must not be a separate numbered line")

    english_lines = (ROOT / "references" / "report-template.md").read_text(encoding="utf-8").splitlines()
    if not any(
        "export txt" in line and "export w4dj" in line
        for line in english_lines
    ):
        errors.append("report-template.md: English W4DJ command must share the export sentence")
    return errors


def validate_compatibility(fixtures: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    documents = {
        item["id"]: item["document"] for item in fixtures.get("valid_documents", [])
    }
    for case in fixtures.get("compatibility_cases", []):
        document = documents.get(case["document_id"])
        if document is None:
            errors.append(f"compatibility case references missing document {case['document_id']!r}")
            continue
        playlist = document["playlist"]
        tracks = document["tracks"]
        if playlist["output_mode"] != case["expected_output_mode"]:
            errors.append(f"{case['document_id']}: output mode changed")
        if [track["position"] for track in tracks] != case["expected_positions"]:
            errors.append(f"{case['document_id']}: positions changed")
        if "expected_versions" in case and [track["version"] for track in tracks] != case["expected_versions"]:
            errors.append(f"{case['document_id']}: versions changed")
        if "expected_dedupe_keys" in case and [track["dedupe_key"] for track in tracks] != case["expected_dedupe_keys"]:
            errors.append(f"{case['document_id']}: dedupe keys changed")
        for field in case.get("expected_unknown_values", []):
            if tracks[0].get(field) not in (None, "unknown"):
                errors.append(f"{case['document_id']}: unknown field {field!r} was invented")
    return errors


def main() -> int:
    errors: list[str] = []
    try:
        if not SCHEMA.exists():
            errors.append(f"missing schema: {SCHEMA}")
        if not FIXTURES.exists():
            errors.append(f"missing fixtures: {FIXTURES}")
        if not errors:
            schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
            fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
            for item in fixtures.get("valid_documents", []):
                errors.extend(validate(item["document"], schema, f"valid.{item['id']}", schema))
            for item in fixtures.get("invalid_documents", []):
                if not validate(item["document"], schema, f"invalid.{item['id']}", schema):
                    errors.append(f"invalid fixture unexpectedly passed: {item['id']}")
            errors.extend(validate_compatibility(fixtures))
            errors.extend(source_contract_errors())
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        errors.append(str(exc))

    if errors:
        print("FAIL: W4DJ contract")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: W4DJ schema, fixtures, compatibility cases, and source contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
