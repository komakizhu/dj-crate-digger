#!/usr/bin/env python3
"""Validate multilingual natural-language platform-policy behavior."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = ROOT / "evals" / "platform-policy-fixtures.json"
LOCALES_DIR = ROOT / "references" / "locales"
JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

LEGACY_ALIASES = {
    "网易云": "netease_cloud_music",
    "网易云音乐": "netease_cloud_music",
    "NetEase Cloud Music": "netease_cloud_music",
    "Apple Music": "apple_music",
    "Spotify": "spotify",
    "SoundCloud": "soundcloud",
    "Bandcamp": "bandcamp",
    "Beatport": "beatport",
    "Beatsource": "beatsource",
}
LEGACY_EXCLUSIVE_MARKERS = ("唯一平台", "仅限", "只使用", "只在", "只要", "仅接受")
LEGACY_PREFERRED_MARKERS = ("优先", "最好有", "备用", "回退")
LEGACY_FORBIDDEN_MARKERS = ("不要", "不提供", "排除")


def load_pack(locale: str) -> dict[str, Any]:
    path = LOCALES_DIR / f"{locale}.md"
    matches = JSON_FENCE_RE.findall(path.read_text(encoding="utf-8"))
    if len(matches) != 1:
        raise ValueError(f"{path}: expected exactly one JSON block")
    value = json.loads(matches[0])
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON block must be an object")
    return value


def policy_for(locale: str | None) -> tuple[dict[str, str], tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    if locale is None:
        aliases = dict(LEGACY_ALIASES)
        return aliases, LEGACY_EXCLUSIVE_MARKERS, LEGACY_PREFERRED_MARKERS, LEGACY_FORBIDDEN_MARKERS
    pack = load_pack(locale)
    policy = pack["platform_policy"]
    aliases = {str(value): str(key) for key, value in policy["aliases"].items()}
    # Canonical English names remain compatible in every localized conversation.
    aliases.update({key: key for key in LEGACY_ALIASES.values()})
    return (
        aliases,
        tuple(policy["exclusive_markers"]),
        tuple(policy["preferred_markers"]),
        tuple(policy["forbidden_markers"]),
    )


def _contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()


def _find_platforms(text: str, aliases: dict[str, str]) -> list[str]:
    matches = sorted(
        (position, canonical)
        for alias, canonical in aliases.items()
        for position in [text.casefold().find(alias.casefold())]
        if position >= 0
    )
    platforms: list[str] = []
    for _, canonical in matches:
        if canonical not in platforms:
            platforms.append(canonical)
    return platforms


def classify_platform_text(text: str, locale: str | None = None) -> tuple[str, list[str]]:
    aliases, exclusive_markers, preferred_markers, _ = policy_for(locale)
    platforms = _find_platforms(text, aliases)
    forbidden = set(extract_forbidden_platforms(text, locale))
    # A forbidden platform is a hard filter, not an allowed platform with a
    # contradictory annotation.  This prevents "do not use Spotify" from
    # being misclassified as a one-platform exclusive request.
    platforms = [platform for platform in platforms if platform not in forbidden]
    has_exclusive_marker = any(_contains(text, marker) for marker in exclusive_markers)
    has_preferred_marker = any(_contains(text, marker) for marker in preferred_markers)
    if has_exclusive_marker or (len(platforms) == 1 and not has_preferred_marker):
        return "exclusive", platforms[:1]
    if len(platforms) > 1 or has_preferred_marker:
        return "preferred", platforms
    return "cross-platform", []


def extract_forbidden_platforms(text: str, locale: str | None = None) -> list[str]:
    aliases, _, _, forbidden_markers = policy_for(locale)
    forbidden: list[str] = []
    for alias, canonical in aliases.items():
        if any(
            re.search(
                rf"(?:{re.escape(marker)}[\s:：,，;；、/\\-]{{0,6}}{re.escape(alias)}|{re.escape(alias)}[\s:：,，;；、/\\-]{{0,6}}{re.escape(marker)})",
                text,
                flags=re.IGNORECASE,
            )
            for marker in forbidden_markers
        ):
            if canonical not in forbidden:
                forbidden.append(canonical)
    return forbidden


def assert_source_contract() -> list[str]:
    source_paths = (
        ROOT / "SKILL.md",
        ROOT / "references" / "search-verification.md",
        ROOT / "references" / "report-template.md",
        ROOT / "references" / "export.md",
    )
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    required_fragments = (
        "locales/manifest.json",
        "locale_pack",
        "communication_language",
        "target_market",
        "action_intent",
        "exclusive",
        "preferred",
        "forbidden",
    )
    return [
        f"source contract missing required phrase: {fragment}"
        for fragment in required_fragments
        if fragment not in source
    ]


def assert_case(case: dict[str, Any], locale: str | None = None) -> list[str]:
    mode, allowed = classify_platform_text(str(case["input"]), locale)
    errors: list[str] = []
    if case.get("mode") is not None and mode != case["mode"]:
        errors.append(f"{case['name']}: expected mode {case['mode']!r}, got {mode!r}")
    if case.get("allowed") is not None and allowed != case["allowed"]:
        errors.append(f"{case['name']}: expected allowed {case['allowed']!r}, got {allowed!r}")
    if case.get("forbidden") is not None:
        forbidden = extract_forbidden_platforms(str(case["input"]), locale)
        if forbidden != case["forbidden"]:
            errors.append(f"{case['name']}: expected forbidden {case['forbidden']!r}, got {forbidden!r}")
    if case.get("missing_behavior") == "target-platform-missing-no-fallback":
        if mode != "exclusive" or len(allowed) != 1:
            errors.append(f"{case['name']}: exclusive missing-platform case lost target-only policy")
    return errors


def assert_locale_smoke() -> list[str]:
    manifest = json.loads((LOCALES_DIR / "manifest.json").read_text(encoding="utf-8"))
    failures: list[str] = []
    for entry in manifest["locales"]:
        locale = str(entry["id"])
        pack = load_pack(locale)
        aliases = pack["platform_policy"]["aliases"]
        spotify = str(aliases["spotify"])
        soundcloud = str(aliases["soundcloud"])
        mode, allowed = classify_platform_text(spotify, locale)
        if mode != "exclusive" or allowed != ["spotify"]:
            failures.append(f"{locale}: one localized platform must default to exclusive")
        mode, allowed = classify_platform_text(f"{spotify} / {soundcloud}", locale)
        if mode != "preferred" or allowed != ["spotify", "soundcloud"]:
            failures.append(f"{locale}: multiple localized platforms must be ordered preferred")
        marker = str(pack["platform_policy"]["forbidden_markers"][0])
        if "spotify" not in extract_forbidden_platforms(f"{marker} {spotify}", locale):
            failures.append(f"{locale}: localized forbidden marker did not exclude Spotify")
    return failures


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FIXTURES
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    failures = assert_source_contract()
    for group in ("exclusive_cases", "preferred_cases", "hard_filter_cases"):
        for case in fixtures[group]:
            failures.extend(assert_case(case))
    for case in fixtures.get("localized_cases", []):
        failures.extend(assert_case(case, str(case["locale"])))
    failures.extend(assert_locale_smoke())
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    case_count = sum(len(fixtures[group]) for group in ("exclusive_cases", "preferred_cases", "hard_filter_cases"))
    localized_count = len(fixtures.get("localized_cases", []))
    print(f"PASS: platform policy contract, {case_count} legacy fixtures, {localized_count} localized fixtures, and 26-locale smoke checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
