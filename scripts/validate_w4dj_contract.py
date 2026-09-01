#!/usr/bin/env python3
"""Validate the current W4DJ handoff contract and source references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "references" / "w4dj.schema.json"
FIXTURES = ROOT / "evals" / "w4dj-fixtures.json"
FORMAT_VERSION_KEY = "format_" + "version"
LEGACY_TRACK_KEYS = {
    "version",
    "version_" + "label",
    "version_" + "kind",
    "version_" + "match",
}


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
    return root_schema["$defs"][reference.removeprefix("#/$defs/")]


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
    if "not" in schema and not validate(value, schema["not"], path, root_schema):
        errors.append(f"{path}: value matches a forbidden schema")
    expected_types = schema.get("type")
    if expected_types is not None:
        types = [expected_types] if isinstance(expected_types, str) else expected_types
        if not any(type_matches(value, expected) for expected in types):
            errors.append(f"{path}: expected type {types!r}")
            return errors
    if isinstance(value, str) and len(value) < schema.get("minLength", 0):
        errors.append(f"{path}: string is shorter than minLength")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get("minimum", value):
            errors.append(f"{path}: number is below minimum")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: array has fewer than minItems")
        if schema.get("items"):
            for index, item in enumerate(value):
                errors.extend(validate(item, schema["items"], f"{path}[{index}]", root_schema))
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


def semantic_contract_errors(document: dict[str, Any], label: str) -> list[str]:
    errors: list[str] = []
    tracks = document.get("tracks")
    if not isinstance(tracks, list):
        return errors
    positions = [track.get("position") for track in tracks if isinstance(track, dict)]
    if len(positions) != len(set(positions)):
        errors.append(f"{label}: track.position values must be unique")
    if positions and positions != list(range(1, len(positions) + 1)):
        errors.append(f"{label}: track.position values must be consecutive")
    for index, track in enumerate(tracks):
        if not isinstance(track, dict):
            continue
        if any(key in track for key in LEGACY_TRACK_KEYS):
            errors.append(f"{label}.tracks[{index}]: legacy title-variant field is forbidden")
        if "title" in track and not isinstance(track["title"], str):
            errors.append(f"{label}.tracks[{index}]: title must be text")
    return errors


def shape_errors(schema: dict[str, Any], fixtures: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    root_properties = schema.get("properties", {})
    expected_root = {"format", FORMAT_VERSION_KEY, "export_id", "playlist", "tracks"}
    if set(root_properties) != expected_root:
        errors.append("W4DJ root properties are not minimal")
    if root_properties.get("format", {}).get("const") != "w4dj":
        errors.append("W4DJ schema format must be 'w4dj'")
    format_version_schema = root_properties.get(FORMAT_VERSION_KEY, {})
    if format_version_schema.get("type") != "integer" or format_version_schema.get("const") != 2:
        errors.append("W4DJ format_version must be the fixed integer 2")
    if set(schema.get("required", [])) != expected_root:
        errors.append("W4DJ root required fields are not minimal")
    playlist_schema = root_properties.get("playlist", {})
    if set(playlist_schema.get("properties", {})) != {"name"}:
        errors.append("W4DJ playlist must contain only name")
    track_schema = schema.get("$defs", {}).get("track", {})
    expected_track = {"position", "title", "artist_display", "netease_track_id"}
    if set(track_schema.get("properties", {})) != expected_track:
        errors.append("W4DJ track fields are not minimal")
    if set(track_schema.get("required", [])) != {"position", "title", "artist_display"}:
        errors.append("W4DJ track required fields are incorrect")
    if track_schema.get("properties", {}).get("netease_track_id", {}).get("type") != "string":
        errors.append("netease_track_id must be a JSON string")
    for item in fixtures.get("valid_documents", []):
        document = item.get("document", {})
        if set(document) != expected_root:
            errors.append(f"{item['id']}: valid root is not minimal")
        if document.get(FORMAT_VERSION_KEY) != 2:
            errors.append(f"{item['id']}: format_version must be the fixed integer 2")
        if set(document.get("playlist", {})) != {"name"}:
            errors.append(f"{item['id']}: valid playlist is not minimal")
        for index, track in enumerate(document.get("tracks", [])):
            if set(track) - expected_track:
                errors.append(f"{item['id']}.tracks[{index}]: contains a legacy or unknown field")
            if "netease_track_id" in track and not isinstance(track["netease_track_id"], str):
                errors.append(f"{item['id']}.tracks[{index}]: netease_track_id is not a string")
    return errors


def compatibility_errors(fixtures: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    documents = {
        item["id"]: item["document"] for item in fixtures.get("valid_documents", [])
    }
    for case in fixtures.get("compatibility_cases", []):
        case_id = case.get("document_id")
        document = documents.get(case_id)
        if document is None:
            errors.append(f"compatibility case references unknown document: {case_id}")
            continue
        if document.get(FORMAT_VERSION_KEY) != 2:
            errors.append(f"{case_id}: compatibility format_version must be 2")
        tracks = document.get("tracks", [])
        actual_positions = [track.get("position") for track in tracks]
        if "expected_positions" in case and actual_positions != case["expected_positions"]:
            errors.append(f"{case_id}: compatibility positions do not match fixture")
        if "expected_titles" in case:
            actual_titles = [track.get("title") for track in tracks]
            if actual_titles != case["expected_titles"]:
                errors.append(f"{case_id}: compatibility titles do not match fixture")
        if "expected_netease_ids" in case:
            actual_ids = [track.get("netease_track_id") for track in tracks]
            if actual_ids != case["expected_netease_ids"]:
                errors.append(f"{case_id}: compatibility NetEase IDs do not match fixture")
    return errors


def source_contract_errors() -> list[str]:
    source_paths = (
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "references" / "export.md",
        ROOT / "references" / "report-template.md",
        ROOT / "references" / "search-verification.md",
    )
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    required = (
        "locales/manifest.json",
        "communication_language",
        "target_market",
        "action_intent",
        "output_text_playlist",
        "export_w4dj",
        ".w4dj",
        "UTF-8 JSON",
        "format_version",
        "integer `2`",
        "netease_track_id",
        "不生成占位文件",
        "不处理本地音频",
    )
    errors = [f"source contract missing {fragment!r}" for fragment in required if fragment not in source]
    retired = (
        "导出" + "t" + "x" + "t",
        "导出" + "w4dj",
        "导出" + "歌单名",
        "." + "t" + "x" + "t",
        "schema " + "v2",
        "w4dj " + "v1",
        "w4dj " + "v2",
        "." + "w4djcrate",
        "local_" + "export",
    )
    for token in retired:
        if token in source:
            errors.append(f"source contract contains retired token {token!r}")
    report_text = (ROOT / "references" / "report-template.md").read_text(encoding="utf-8")
    if "locale_pack" not in report_text or "action_intent" not in report_text:
        errors.append("report-template.md: visible text is not routed through locale packs and action intents")
    return errors


def main() -> int:
    errors: list[str] = []
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
        for item in fixtures.get("valid_documents", []):
            errors.extend(validate(item["document"], schema, f"valid.{item['id']}", schema))
            errors.extend(semantic_contract_errors(item["document"], f"valid.{item['id']}"))
        for item in fixtures.get("invalid_documents", []):
            schema_errors = validate(item["document"], schema, f"invalid.{item['id']}", schema)
            semantic_errors = semantic_contract_errors(item["document"], f"invalid.{item['id']}")
            if not schema_errors and not semantic_errors:
                errors.append(f"invalid fixture unexpectedly passed: {item['id']}")
        errors.extend(shape_errors(schema, fixtures))
        errors.extend(compatibility_errors(fixtures))
        errors.extend(source_contract_errors())
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    if errors:
        print("FAIL: W4DJ contract")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: W4DJ schema, fixtures, and source contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
