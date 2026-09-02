#!/usr/bin/env python3
"""Project the central trigger contract into every locale trigger resource."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from trigger_router import classify


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "references" / "trigger-signals.json"
MANIFEST_PATH = ROOT / "references" / "locales" / "manifest.json"
LOCALE_SOURCE_DIR = ROOT / "references" / "locales"
STAGE_KEYS = (
    "mode",
    "dj_action",
    "dj_object",
    "dj_context",
    "reference",
    "set_detail",
    "genre_context",
    "generic_music_term",
    "negative_context",
    "explanatory_context",
)
JSON_FENCE_RE = re.compile(r"(```json\s*\n)(.*?)(\n```)", re.DOTALL)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected an object")
    return value


def semantic_overlay(contract: dict[str, Any], locale: str) -> dict[str, Any]:
    overlays = contract.get("locale_overlays", {})
    overlay = overlays.get(locale)
    if not isinstance(overlay, dict):
        raise ValueError(f"missing locale overlay: {locale}")
    shared = contract.get("shared_signal_terms", {})
    result: dict[str, Any] = {}
    for key in STAGE_KEYS:
        if key in overlay:
            result[key] = overlay[key]
        elif key == "genre_context":
            result[key] = shared.get(key, [])
        else:
            result[key] = []
    result["genre_families"] = list(contract.get("genre_families", {}))
    return result


def capsule_additions(contract: dict[str, Any], locale: str) -> list[str]:
    overlay = contract["locale_overlays"][locale]
    additions: list[str] = []
    modes = overlay.get("mode", {})
    for mode in ("fast", "composite", "four_views"):
        labels = modes.get(mode, []) if isinstance(modes, dict) else []
        if labels:
            additions.append(labels[0])
    for key in ("dj_action", "dj_object", "dj_context"):
        values = overlay.get(key, [])
        if isinstance(values, list) and values:
            additions.append(values[0])
    additions.extend(("house", "techno", "drum & bass", "jungle"))
    return additions


def update_stage(path: Path, locale: str, contract: dict[str, Any]) -> None:
    payload = load_json(path)
    overlay = contract["locale_overlays"][locale]
    direct = list(payload.get("direct", []))
    ambiguous = list(payload.get("ambiguous", []))
    for term in overlay.get("dj_action", []):
        if classify(term, locale, contract=contract)["skill_route"] == "direct" and term not in direct:
            direct.append(term)
    for term in overlay.get("generic_music_term", []):
        if classify(term, locale, contract=contract)["skill_route"] == "ambiguous" and term not in ambiguous:
            ambiguous.append(term)
    payload["direct"] = direct
    payload["ambiguous"] = [
        term
        for term in ambiguous
        if term not in direct
        and classify(term, locale, contract=contract)["skill_route"] != "direct"
    ]
    payload["trigger_contract"] = {
        "path": "references/trigger-signals.json",
        "version": contract.get("version"),
    }
    payload["semantic_signals"] = semantic_overlay(contract, locale)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_locale_markdown(path: Path, locale: str, contract: dict[str, Any]) -> None:
    text = path.read_text(encoding="utf-8")
    match = JSON_FENCE_RE.search(text)
    if not match or len(JSON_FENCE_RE.findall(text)) != 1:
        raise ValueError(f"{path}: expected exactly one JSON code block")
    payload = json.loads(match.group(2))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: locale payload must be an object")
    payload["trigger_contract"] = {
        "path": "references/trigger-signals.json",
        "version": contract.get("version"),
    }
    payload["trigger_signal_families"] = list(STAGE_KEYS) + ["genre_families"]
    capsule = payload.get("trigger_capsule", [])
    if not isinstance(capsule, list):
        capsule = []
    for value in capsule_additions(contract, locale):
        if value not in capsule:
            capsule.append(value)
    payload["trigger_capsule"] = capsule
    # Keep Markdown fences inside prompt string values escaped.  The locale
    # validator must be able to distinguish the one outer JSON fence from the
    # fill-in template embedded in the JSON payload.
    block = json.dumps(payload, ensure_ascii=False, indent=2).replace(
        "```", r"\u0060\u0060\u0060"
    )
    updated = text[: match.start(2)] + block + text[match.end(2) :]
    path.write_text(updated, encoding="utf-8")


def materialize(apply: bool) -> list[str]:
    contract = load_json(CONTRACT_PATH)
    manifest = load_json(MANIFEST_PATH)
    changed: list[str] = []
    for entry in manifest.get("locales", []):
        locale = entry["id"]
        stage_map = manifest["locale_progressive_resources"][locale]
        stage_path = ROOT / stage_map["trigger"]
        locale_path = LOCALE_SOURCE_DIR / entry["file"]
        if apply:
            update_stage(stage_path, locale, contract)
            update_locale_markdown(locale_path, locale, contract)
        changed.extend([str(stage_path.relative_to(ROOT)), str(locale_path.relative_to(ROOT))])
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the projected resources")
    args = parser.parse_args()
    try:
        changed = materialize(args.apply)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    action = "updated" if args.apply else "would update"
    print(f"PASS: {action} {len(changed) // 2} locale trigger projections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
