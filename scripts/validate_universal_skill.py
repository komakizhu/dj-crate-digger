#!/usr/bin/env python3
"""Validate the universal Agent Skill package and its zero-legacy contract."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "evals" / "universal-skill-fixtures.json"
MANIFEST = ROOT / "references" / "locales" / "manifest.json"
LEGACY_TOKENS = (
    "导出" + "t" + "x" + "t",
    "导出" + "w4dj",
    "导出" + "歌单名",
    "." + "t" + "x" + "t",
    "schema " + "v2",
    "w4dj " + "v1",
    "." + "w4djcrate",
    "local_" + "export",
    "version_" + "label",
    "version_" + "kind",
    "version_" + "match",
    "m" + "3u8",
)


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return [ROOT / line for line in result.stdout.splitlines() if line]


def locale_pack(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    matches = re.findall(r"```json\s*\n(.*?)\n```", content, flags=re.DOTALL)
    if len(matches) != 1:
        raise ValueError(f"{path}: expected exactly one JSON block")
    return json.loads(matches[0])


def main() -> int:
    errors: list[str] = []
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    skill_path = ROOT / "SKILL.md"
    skill_lines = skill_path.read_text(encoding="utf-8").splitlines()
    if len(skill_lines) > fixtures["max_controller_lines"]:
        errors.append(
            f"SKILL.md controller has {len(skill_lines)} lines; expected <= {fixtures['max_controller_lines']}"
        )

    if skill_lines[:1] != ["---"]:
        errors.append("SKILL.md is missing YAML frontmatter")
    else:
        try:
            end = skill_lines.index("---", 1)
            frontmatter = skill_lines[1:end]
        except ValueError:
            frontmatter = []
            errors.append("SKILL.md frontmatter is not closed")
        fields = [line.split(":", 1)[0].strip() for line in frontmatter if ":" in line]
        if fields != ["name", "description"]:
            errors.append(f"SKILL.md frontmatter must contain only name and description, got {fields}")
        required_skill_name = fixtures.get("required_skill_name")
        if f"name: {required_skill_name}" not in frontmatter:
            errors.append(f"SKILL.md name must be {required_skill_name}")
        description = next((line for line in frontmatter if line.startswith("description:")), "")
        description_value = description.split(":", 1)[1].strip().strip('"').strip("'")
        if not description_value.startswith("Use when"):
            errors.append("SKILL.md description must start with 'Use when'")
        if len("\n".join(frontmatter)) > 1024:
            errors.append("SKILL.md frontmatter exceeds 1024 characters")

    core_text = skill_path.read_text(encoding="utf-8")
    for host_name in ("Codex", "Claude", "Gemini", "Cursor", "Windsurf", "Qoder", "Trae", "WorkBuddy", "CodeBuddy", "OpenCode"):
        if host_name.lower() in core_text.lower():
            errors.append(f"host-specific name {host_name!r} leaked into SKILL.md")

    for relative in fixtures["required_resources"]:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing progressive resource: {relative}")

    language_resource = ROOT / "references" / "language-routing.json"
    if language_resource.exists():
        try:
            language_policy = json.loads(language_resource.read_text(encoding="utf-8"))
            required_capabilities = set(fixtures.get("required_language_capabilities", []))
            configured_capabilities = set(language_policy.get("optional_capabilities", []))
            if not required_capabilities <= configured_capabilities:
                errors.append("language routing policy omits required optional capabilities")
        except (OSError, json.JSONDecodeError, TypeError):
            errors.append("language routing policy cannot be loaded")

    schema_path = ROOT / "references" / "w4dj.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        expected_root = set(fixtures.get("required_w4dj_root_fields", []))
        expected_track = set(fixtures.get("required_w4dj_track_fields", []))
        if set(schema.get("properties", {})) != expected_root:
            errors.append("W4DJ schema root does not match universal fixture contract")
        required_version = fixtures.get("required_w4dj_format_version")
        version_schema = schema.get("properties", {}).get("format_version", {})
        if version_schema.get("type") != "integer" or version_schema.get("const") != required_version:
            errors.append("W4DJ schema does not enforce the fixed compatibility format version")
        if set(schema.get("$defs", {}).get("track", {}).get("properties", {})) != expected_track:
            errors.append("W4DJ schema track fields do not match universal fixture contract")
    except (OSError, json.JSONDecodeError, TypeError):
        errors.append("W4DJ schema cannot be loaded for universal contract checks")

    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        progressive = manifest.get("progressive_resources", {})
        for key, relative in progressive.items():
            if not isinstance(relative, str) or not (ROOT / relative).exists():
                errors.append(f"missing progressive resource mapping: {key}")
        entries = manifest.get("locales", [])
        if len(entries) != 26:
            errors.append(f"locale manifest has {len(entries)} entries, expected 26")
        for entry in entries:
            path = ROOT / "references" / "locales" / entry.get("file", "")
            if not path.exists():
                errors.append(f"missing locale pack: {path}")
            else:
                try:
                    pack = locale_pack(path)
                    if pack.get("locale") != entry.get("id"):
                        errors.append(f"locale metadata mismatch: {path}")
                except (OSError, ValueError, json.JSONDecodeError) as exc:
                    errors.append(str(exc))
        expected_stage_keys = set(fixtures.get("required_locale_stage_keys", []))
        locale_stage_map = manifest.get("locale_progressive_resources", {})
        if not isinstance(locale_stage_map, dict) or set(locale_stage_map) != {
            entry.get("id") for entry in entries if isinstance(entry, dict)
        }:
            errors.append("locale progressive resource map does not cover the 26 locale packs")
        else:
            for locale, mapping in locale_stage_map.items():
                if not isinstance(mapping, dict) or set(mapping) != expected_stage_keys:
                    errors.append(f"locale {locale} has incomplete stage resource mapping")
                    continue
                for stage, relative in mapping.items():
                    path = ROOT / relative if isinstance(relative, str) else None
                    if path is None or not path.exists():
                        errors.append(f"missing locale stage resource: {locale}.{stage}")
                        continue
                    try:
                        payload = json.loads(path.read_text(encoding="utf-8"))
                        if payload.get("locale") != locale or payload.get("stage") != stage:
                            errors.append(f"locale stage metadata mismatch: {path}")
                    except (OSError, json.JSONDecodeError, AttributeError) as exc:
                        errors.append(f"invalid locale stage resource {path}: {exc}")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8") + (ROOT / "README.en.md").read_text(encoding="utf-8")
    for agent_reference in fixtures["supported_agent_references"]:
        if agent_reference.lower() not in readme_text.lower():
            errors.append(f"README compatibility matrix omits {agent_reference}")
    for pending_reference in fixtures.get("pending_agent_references", []):
        if pending_reference.lower() not in readme_text.lower():
            errors.append(f"README pending compatibility note omits {pending_reference}")

    for source in (skill_path, ROOT / "references" / "report-template.md"):
        for target in re.findall(r"\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            target_path = (source.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                errors.append(f"broken relative resource link in {source.relative_to(ROOT)}: {target}")
    if not MANIFEST.exists():
        errors.append("missing locale manifest")

    for path in tracked_files():
        if not path.exists():
            continue
        if "docs/w4dj/" in path.relative_to(ROOT).as_posix():
            continue
        if path.suffix not in {".md", ".json", ".py", ".yaml", ".yml"}:
            continue
        content = path.read_text(encoding="utf-8").lower()
        for token in LEGACY_TOKENS:
            if token.lower() in content:
                errors.append(f"legacy token {token!r} remains in {path.relative_to(ROOT)}")

    if errors:
        print("FAIL: universal Agent Skill contract")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: universal Agent Skill structure and zero-legacy contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
