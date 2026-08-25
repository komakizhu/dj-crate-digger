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
    )
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    required = (
        "导出到w4dj",
        "输出文字版歌单",
        ".w4dj",
        "UTF-8 JSON",
        "w4dj.schema.json",
        "format_version: 2",
        "netease_track_id",
        "v1",
        "不做迁移",
        "只保留",
        "未知",
        "不生成占位文件",
        "不处理本地音频",
    )
    errors = [f"source contract missing {fragment!r}" for fragment in required if fragment not in source]

    concise_track_list_notice = (
        "`输出文字版歌单`的功能：输出可复制文本，可以手动导入网易云，但无法帮您一键把歌曲导入 RKB。"
    )
    old_track_list_notice = (
        "导出歌单名的功能：输出标题“## 网易云歌单目录”，并在标题下方用 Markdown 代码围栏包住"
    )
    user_template_paths = (
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "references" / "export.md",
        ROOT / "references" / "report-template.md",
    )
    for path in user_template_paths:
        text = path.read_text(encoding="utf-8")
        if concise_track_list_notice not in text:
            errors.append(f"{path.name}: missing concise track-list export notice")
        if old_track_list_notice in text:
            errors.append(f"{path.name}: contains the old verbose track-list export notice")

        for old_command in ("导出w4dj", "导出歌单名"):
            if old_command in text:
                errors.append(f"{path.name}: contains retired export command {old_command!r}")
        for old_format_marker in ("schema v1", "format_version: 1", "格式版本固定为 `1`"):
            if old_format_marker in text:
                errors.append(f"{path.name}: contains retired W4DJ format marker {old_format_marker!r}")

    short_skill_link = "[dj-crate-digger](https://github.com/komakizhu/dj-crate-digger)"
    for path in (ROOT / "SKILL.md", ROOT / "references" / "report-template.md"):
        if short_skill_link not in path.read_text(encoding="utf-8"):
            errors.append(f"{path.name}: repository tutorial link must use the short label")

    chinese_template_paths = (
        ROOT / "SKILL.md",
        ROOT / "references" / "report-template.md",
    )
    for path in chinese_template_paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        export_lines = [line for line in lines if "输出文字版歌单" in line]
        if not any("导出到w4dj" in line for line in export_lines):
            errors.append(f"{path.name}: W4DJ must share the track-list export sentence")
        if any("您可以把本次推荐交接给 W4DJ" in line for line in lines):
            errors.append(f"{path.name}: W4DJ must not be a separate numbered line")

    english_lines = (ROOT / "references" / "report-template.md").read_text(encoding="utf-8").splitlines()
    if not any(
        "output text playlist" in line and "export to w4dj" in line
        for line in english_lines
    ):
        errors.append("report-template.md: English W4DJ command must share the track-list export sentence")
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
