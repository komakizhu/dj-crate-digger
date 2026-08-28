#!/usr/bin/env python3
"""Validate the W4DJ handoff schema, fixtures, and documented Skill contract."""

from __future__ import annotations

import json
import re
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

    if "not" in schema and not validate(value, schema["not"], path, root_schema):
        errors.append(f"{path}: value matches a forbidden schema")

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
        ROOT / "references" / "search-verification.md",
    )
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    required = (
        "locales/manifest.json",
        "locale_pack",
        "communication_language",
        "target_market",
        "action_intent",
        "output_text_playlist",
        "export_w4dj",
        ".w4dj",
        "UTF-8 JSON",
        "format_version: 2",
        "netease_track_id",
        "不生成占位文件",
        "不处理本地音频",
    )
    errors = [f"source contract missing {fragment!r}" for fragment in required if fragment not in source]

    for old_command in ("导出w4dj", "导出歌单名"):
        if old_command in source:
            errors.append(f"source contract contains retired export command {old_command!r}")

    report_text = (ROOT / "references" / "report-template.md").read_text(encoding="utf-8")
    if "locale_pack.report" not in report_text or "action_intent" not in report_text:
        errors.append("report-template.md: visible text is not routed through locale packs and action intents")

    manifest_path = ROOT / "references" / "locales" / "manifest.json"
    locale_dir = ROOT / "references" / "locales"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entries = manifest["locales"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        return errors + [f"locale manifest cannot be read by W4DJ contract: {exc}"]
    if len(entries) != 26:
        errors.append(f"locale manifest: expected 26 entries, got {len(entries)}")
    for entry in entries:
        locale = entry.get("id")
        filename = entry.get("file")
        if not isinstance(locale, str) or not isinstance(filename, str):
            errors.append("locale manifest: malformed entry")
            continue
        pack_path = locale_dir / filename
        if not pack_path.exists():
            errors.append(f"locale manifest: missing {filename}")
            continue
        try:
            matches = re.findall(
                r"```json\s*\n(.*?)\n```",
                pack_path.read_text(encoding="utf-8"),
                flags=re.DOTALL,
            )
            pack = json.loads(matches[0])
        except (OSError, json.JSONDecodeError, IndexError, TypeError) as exc:
            errors.append(f"{locale}: invalid locale pack in source contract: {exc}")
            continue
        if pack.get("locale") != locale:
            errors.append(f"{locale}: locale pack metadata mismatch")
        tutorial_url = str(pack.get("quick_start", {}).get("tutorial_url", ""))
        expected_tutorial = "/docs/w4dj/README.md" if locale.startswith("zh-") else "/docs/w4dj/README.en.md"
        if expected_tutorial not in tutorial_url:
            errors.append(f"{locale}: tutorial link is not localized to the documented language")
    return errors

def title_embedded_version_errors(schema: dict[str, Any], fixtures: dict[str, Any]) -> list[str]:
    """Enforce that an official title carries its own Remix/Edit/Live qualifier."""
    errors: list[str] = []
    track_schema = schema.get("$defs", {}).get("track", {})
    track_properties = track_schema.get("properties", {})
    if "version" in track_properties:
        errors.append("W4DJ track schema must not expose a separate 'version' field")
    if "version" in track_schema.get("required", []):
        errors.append("W4DJ track schema must not require a separate 'version' field")

    qualifier_seen = False
    qualifiers = ("Remix", "Edit", "Live", "Dub", "Instrumental", "Radio Edit", "Extended Mix")
    for item in fixtures.get("valid_documents", []):
        for index, track in enumerate(item.get("document", {}).get("tracks", [])):
            if "version" in track:
                errors.append(
                    f"{item['id']}.tracks[{index}]: version qualifier must be part of title"
                )
            if any(qualifier in track.get("title", "") for qualifier in qualifiers):
                qualifier_seen = True
    if not qualifier_seen:
        errors.append("valid fixtures must cover a title with an embedded official qualifier")
    return errors


def v2_shape_errors(schema: dict[str, Any], fixtures: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    root_properties = schema.get("properties", {})
    if set(root_properties) != {"format", "format_version", "export_id", "playlist", "tracks"}:
        errors.append("W4DJ v2 root properties are not minimal")
    if root_properties.get("format", {}).get("const") != "w4dj":
        errors.append("W4DJ schema format must be 'w4dj'")
    if root_properties.get("format_version", {}).get("const") != 2:
        errors.append("W4DJ schema must require format_version 2")

    root_required = set(schema.get("required", []))
    if root_required != {"format", "format_version", "export_id", "playlist", "tracks"}:
        errors.append("W4DJ v2 root required fields are not minimal")

    playlist_schema = root_properties.get("playlist", {})
    if set(playlist_schema.get("properties", {})) != {"name"}:
        errors.append("W4DJ v2 playlist must contain only name")

    track_schema = schema.get("$defs", {}).get("track", {})
    track_properties = set(track_schema.get("properties", {}))
    if track_properties != {"position", "title", "artist_display", "netease_track_id"}:
        errors.append("W4DJ v2 track fields are not minimal")
    if set(track_schema.get("required", [])) != {"position", "title", "artist_display"}:
        errors.append("W4DJ v2 track required fields are incorrect")
    if track_schema.get("properties", {}).get("netease_track_id", {}).get("type") != "string":
        errors.append("netease_track_id must be a JSON string")

    for item in fixtures.get("valid_documents", []):
        document = item.get("document", {})
        if document.get("format_version") != 2:
            errors.append(f"{item['id']}: valid fixture is not format_version 2")
        if set(document.get("playlist", {})) != {"name"}:
            errors.append(f"{item['id']}: valid fixture playlist is not minimal")
        for index, track in enumerate(document.get("tracks", [])):
            if set(track) - {"position", "title", "artist_display", "netease_track_id"}:
                errors.append(f"{item['id']}.tracks[{index}]: contains a legacy or unknown field")
            if "netease_track_id" in track and not isinstance(track["netease_track_id"], str):
                errors.append(f"{item['id']}.tracks[{index}]: netease_track_id is not a string")
    return errors


def semantic_contract_errors(document: dict[str, Any], label: str) -> list[str]:
    errors: list[str] = []
    tracks = document.get("tracks")
    if not isinstance(tracks, list):
        return errors
    positions = [track.get("position") for track in tracks if isinstance(track, dict)]
    duplicates = sorted({position for position in positions if positions.count(position) > 1})
    if duplicates:
        errors.append(f"{label}: track.position values must be unique: {duplicates}")
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
        tracks = document["tracks"]
        if [track["position"] for track in tracks] != case["expected_positions"]:
            errors.append(f"{case['document_id']}: positions changed")
        if "expected_titles" in case and [track["title"] for track in tracks] != case["expected_titles"]:
            errors.append(f"{case['document_id']}: titles changed")
        if "expected_netease_ids" in case:
            actual_ids = [track.get("netease_track_id") for track in tracks]
            if actual_ids != case["expected_netease_ids"]:
                errors.append(f"{case['document_id']}: NetEase IDs changed")
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
                errors.extend(semantic_contract_errors(item["document"], f"valid.{item['id']}"))
            for item in fixtures.get("invalid_documents", []):
                schema_errors = validate(item["document"], schema, f"invalid.{item['id']}", schema)
                semantic_errors = semantic_contract_errors(item["document"], f"invalid.{item['id']}")
                if not schema_errors and not semantic_errors:
                    errors.append(f"invalid fixture unexpectedly passed: {item['id']}")
            errors.extend(v2_shape_errors(schema, fixtures))
            errors.extend(validate_compatibility(fixtures))
            errors.extend(source_contract_errors())
            errors.extend(title_embedded_version_errors(schema, fixtures))
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
