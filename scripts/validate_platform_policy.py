#!/usr/bin/env python3
"""Validate the documented natural-language platform-policy contract.

This is a regression specification for a prompt-driven Skill, not a production
platform resolver. It checks that the source documents state the contract and
that the representative language matrix maps to the intended policy modes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = ROOT / "evals" / "platform-policy-fixtures.json"

PLATFORM_ALIASES = {
    "网易云": "netease_cloud_music",
    "网易云音乐": "netease_cloud_music",
    "Apple Music": "apple_music",
    "Spotify": "spotify",
    "SoundCloud": "soundcloud",
    "Bandcamp": "bandcamp",
    "Beatport": "beatport",
    "Beatsource": "beatsource",
}
EXCLUSIVE_MARKERS = ("唯一平台", "仅限", "只使用", "只在", "只要", "仅接受")
PREFERRED_MARKERS = ("优先", "最好有", "备用", "回退")


def classify_platform_text(text: str) -> tuple[str, list[str]]:
    matches = sorted(
        (
            position,
            canonical,
        )
        for alias, canonical in PLATFORM_ALIASES.items()
        for position in [text.find(alias)]
        if position >= 0
    )
    platforms: list[str] = []
    for _, canonical in matches:
        if canonical not in platforms:
            platforms.append(canonical)

    has_exclusive_marker = any(marker in text for marker in EXCLUSIVE_MARKERS)
    has_preferred_marker = any(marker in text for marker in PREFERRED_MARKERS)
    if has_exclusive_marker or (len(platforms) == 1 and not has_preferred_marker):
        return "exclusive", platforms[:1]
    if len(platforms) > 1 or has_preferred_marker:
        return "preferred", platforms
    return "cross-platform", []


def extract_forbidden_platforms(text: str) -> list[str]:
    forbidden: list[str] = []
    for alias, canonical in PLATFORM_ALIASES.items():
        marker = rf"(?:不要|不提供)\s*{re.escape(alias)}"
        if re.search(marker, text) and canonical not in forbidden:
            forbidden.append(canonical)
    return forbidden


def assert_source_contract() -> list[str]:
    source_paths = (
        ROOT / "SKILL.md",
        ROOT / "references" / "search-verification.md",
        ROOT / "references" / "report-template.md",
    )
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    required_fragments = (
        "唯一平台",
        "仅限",
        "只使用",
        "只在",
        "只要",
        "仅接受",
        "只填写一个平台",
        "exclusive",
        "目标平台缺失",
        "不把其他平台",
    )
    return [
        f"source contract missing required phrase: {fragment}"
        for fragment in required_fragments
        if fragment not in source
    ]


def assert_case(case: dict[str, object]) -> list[str]:
    mode, allowed = classify_platform_text(str(case["input"]))
    errors: list[str] = []
    expected_mode = case.get("mode")
    if expected_mode is not None and mode != expected_mode:
        errors.append(
            f"{case['name']}: expected mode {expected_mode!r}, got {mode!r}"
        )
    expected_allowed = case.get("allowed")
    if expected_allowed is not None and allowed != expected_allowed:
        errors.append(
            f"{case['name']}: expected allowed {expected_allowed!r}, got {allowed!r}"
        )
    expected_forbidden = case.get("forbidden")
    if expected_forbidden is not None:
        forbidden = extract_forbidden_platforms(str(case["input"]))
        if forbidden != expected_forbidden:
            errors.append(
                f"{case['name']}: expected forbidden {expected_forbidden!r}, got {forbidden!r}"
            )
    if case.get("missing_behavior") == "target-platform-missing-no-fallback":
        if mode != "exclusive" or len(allowed) != 1:
            errors.append(
                f"{case['name']}: exclusive missing-platform case lost its target-only policy"
            )
    return errors


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FIXTURES
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    failures = assert_source_contract()
    groups = ("exclusive_cases", "preferred_cases", "hard_filter_cases")
    for group in groups:
        for case in fixtures[group]:
            failures.extend(assert_case(case))

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    case_count = sum(len(fixtures[group]) for group in groups)
    print(f"PASS: platform policy contract and {case_count} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
