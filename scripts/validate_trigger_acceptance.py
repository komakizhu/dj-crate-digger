#!/usr/bin/env python3
"""Validate the 100-case trigger contract at the portable reference seam."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from trigger_router import classify
from validate_intake_routing import route as intake_route


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "evals" / "trigger-evals.json"
EXPECTED_LOCALES = (
    "en", "zh-Hans", "zh-Hant", "es", "pt", "fr", "de", "ja", "ko", "ar",
    "ru", "tr", "hi", "id", "vi", "th", "it", "nl", "pl", "uk", "fa", "bn",
    "ur", "ms", "fil", "sw",
)
EXPECTED_CASE_TYPES = {
    "baseline_direct",
    "baseline_ambiguous",
    "baseline_negative",
    "stress_mode",
    "stress_genre",
    "stress_normalization",
    "stress_mixed_language",
    "stress_negative_override",
}
EXPECTED_SKILL_ROUTES = {"direct", "ambiguous_confirmation", "non_trigger"}
EXPECTED_HOST_INVOCATIONS = {"must_invoke", "must_not_invoke"}
EXPECTED_CONFIDENCE = {"very_high", "high", "medium", "low"}
EXPECTED_INTAKE_ROUTES = {"direct_ready", "route_choice_pending", "round_1", "not_applicable"}
REQUIRED_CASE_KEYS = {
    "id",
    "case_type",
    "locale",
    "language",
    "input",
    "query",
    "style_family",
    "signal_families",
    "expected_confidence",
    "expected_host_invocation",
    "expected_skill_route",
    "expected_intake_route",
    "intake_signals",
    "should_trigger",
}
VALID_SIGNAL_FAMILIES = {
    "mode",
    "dj_action",
    "dj_object",
    "dj_context",
    "genre",
    "genre_context",
    "reference",
    "set_detail",
    "generic_music_term",
    "negative_context",
    "explanatory_context",
}


def validate_cases(cases: Any) -> list[str]:
    if not isinstance(cases, list):
        return ["trigger acceptance fixture must be a list"]
    errors: list[str] = []
    if len(cases) != 100:
        errors.append(f"trigger acceptance fixture must contain exactly 100 cases, got {len(cases)}")
    ids: set[str] = set()
    by_locale: dict[str, list[dict[str, Any]]] = {locale: [] for locale in EXPECTED_LOCALES}
    stress_counts: dict[str, int] = {}
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case[{index}] must be an object")
            continue
        missing = REQUIRED_CASE_KEYS - set(case)
        if missing:
            errors.append(f"case[{index}] missing fields: {sorted(missing)}")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"case[{index}] id must be non-empty")
        elif case_id in ids:
            errors.append(f"duplicate case id: {case_id}")
        else:
            ids.add(case_id)
        locale = case.get("locale")
        if locale not in EXPECTED_LOCALES:
            errors.append(f"{case_id}: unsupported locale {locale!r}")
        elif isinstance(case, dict) and str(case.get("case_type", "")).startswith("baseline_"):
            by_locale[locale].append(case)
        case_type = case.get("case_type")
        if case_type not in EXPECTED_CASE_TYPES:
            errors.append(f"{case_id}: unsupported case_type {case_type!r}")
        else:
            stress_counts[case_type] = stress_counts.get(case_type, 0) + 1
        if not isinstance(case.get("language"), str) or not case.get("language", "").strip():
            errors.append(f"{case_id}: language must be non-empty")
        if not isinstance(case.get("input"), str) or not case.get("input", "").strip():
            errors.append(f"{case_id}: input must be non-empty")
        if case.get("query") != case.get("input"):
            errors.append(f"{case_id}: query must remain an alias of input for legacy compatibility")
        if not isinstance(case.get("style_family"), str) or not case.get("style_family", "").strip():
            errors.append(f"{case_id}: style_family must be non-empty or 'none'")
        if not isinstance(case.get("signal_families"), list) or not case.get("signal_families"):
            errors.append(f"{case_id}: signal_families must be a non-empty list")
        elif any(family not in VALID_SIGNAL_FAMILIES for family in case["signal_families"]):
            errors.append(f"{case_id}: signal_families contains an unsupported family")
        if case.get("expected_confidence") not in EXPECTED_CONFIDENCE:
            errors.append(f"{case_id}: invalid expected_confidence")
        if case.get("expected_host_invocation") not in EXPECTED_HOST_INVOCATIONS:
            errors.append(f"{case_id}: invalid expected_host_invocation")
        if case.get("expected_skill_route") not in EXPECTED_SKILL_ROUTES:
            errors.append(f"{case_id}: invalid expected_skill_route")
        if case.get("expected_intake_route") not in EXPECTED_INTAKE_ROUTES:
            errors.append(f"{case_id}: invalid expected_intake_route")
        if case.get("expected_skill_route") == "direct" and case.get("expected_intake_route") == "not_applicable":
            errors.append(f"{case_id}: direct route must declare an intake route")
        if case.get("expected_skill_route") != "direct" and case.get("expected_intake_route") != "not_applicable":
            errors.append(f"{case_id}: non-direct route must use not_applicable intake route")
        if not isinstance(case.get("intake_signals"), dict):
            errors.append(f"{case_id}: intake_signals must be an object")
        elif case.get("expected_skill_route") == "direct":
            try:
                actual_intake = intake_route(case["intake_signals"])
                expected_intake = case.get("expected_intake_route")
                if actual_intake.get("route") != expected_intake:
                    errors.append(
                        f"{case_id}: intake expected {expected_intake!r}, got {actual_intake.get('route')!r}"
                    )
            except (TypeError, ValueError) as exc:
                errors.append(f"{case_id}: invalid intake_signals: {exc}")
        expected_should_trigger = case.get("expected_skill_route") == "direct"
        if case.get("should_trigger") != expected_should_trigger:
            errors.append(f"{case_id}: should_trigger must preserve the direct-route compatibility value")
        if "expected_route" in case and case.get("expected_route") != case.get("expected_skill_route"):
            errors.append(f"{case_id}: expected_route must match expected_skill_route")

        if case.get("case_type", "").startswith("stress_"):
            continue

    for locale, locale_cases in by_locale.items():
        if len(locale_cases) != 3:
            errors.append(f"{locale}: expected 3 baseline cases, got {len(locale_cases)}")
            continue
        actual_types = {case.get("case_type") for case in locale_cases}
        expected_types = {"baseline_direct", "baseline_ambiguous", "baseline_negative"}
        if actual_types != expected_types:
            errors.append(f"{locale}: baseline types must be {sorted(expected_types)}, got {sorted(actual_types)}")

    expected_stress_counts = {
        "stress_mode": 6,
        "stress_genre": 6,
        "stress_normalization": 4,
        "stress_mixed_language": 3,
        "stress_negative_override": 3,
    }
    for case_type, expected in expected_stress_counts.items():
        if stress_counts.get(case_type, 0) != expected:
            errors.append(f"{case_type}: expected {expected} cases, got {stress_counts.get(case_type, 0)}")
    if sum(stress_counts.get(case_type, 0) for case_type in expected_stress_counts) != 22:
        errors.append("stress cases must total exactly 22")
    return errors


def validate_reference_behavior(cases: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    for case in cases:
        result = classify(case["input"], case["locale"])
        case_id = case["id"]
        if result["skill_route"] != case["expected_skill_route"]:
            errors.append(
                f"{case_id}: reference skill route expected {case['expected_skill_route']!r}, got {result['skill_route']!r}"
            )
        if result["host_invocation"] != case["expected_host_invocation"]:
            errors.append(
                f"{case_id}: reference host invocation expected {case['expected_host_invocation']!r}, got {result['host_invocation']!r}"
            )
        if result["confidence"] != case["expected_confidence"]:
            errors.append(
                f"{case_id}: confidence expected {case['expected_confidence']!r}, got {result['confidence']!r}"
            )
    by_id = {case.get("id"): case for case in cases}
    normalization_expectations = {
        "stress-normalization-1": "挖歌",
        "stress-normalization-2": "BUILD A DJ SET",
        "stress-normalization-3": "排一个 set",
        "stress-normalization-4": "帮我排一个set 张三妹john summit风格的 edm house 综合版 8首歌",
    }
    for case_id, expected_text in normalization_expectations.items():
        if expected_text not in str(by_id.get(case_id, {}).get("input", "")):
            errors.append(f"{case_id}: normalization stress input is missing {expected_text!r}")
    repeated = str(by_id.get("stress-mixed-language-1", {}).get("input", ""))
    if repeated.count("House") < 3:
        errors.append("stress-mixed-language-1: repeated style signal must occur at least three times")
    genre_families: set[str] = set()
    for case in cases:
        if case.get("case_type") != "stress_genre":
            continue
        genre_families.update(classify(case["input"], case["locale"])["matches"].get("genre", {}))
    expected_genres = {
        "house", "disco", "techno", "dubstep", "bass", "drum_and_bass", "breakbeat", "jungle",
        "garage", "trance", "psytrance", "progressive", "electro", "future_bass", "big_room",
        "hard_dance", "hardcore", "melodic_techno",
    }
    missing_genres = sorted(expected_genres - genre_families)
    if missing_genres:
        errors.append(f"stress genre cases do not cover families: {missing_genres}")
    return errors


def validate_file(path: Path = FIXTURE_PATH) -> list[str]:
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load trigger acceptance fixture: {exc}"]
    errors = validate_cases(cases)
    if not errors and isinstance(cases, list):
        errors.extend(validate_reference_behavior(cases))
    return errors


def main() -> int:
    errors = validate_file()
    if errors:
        print("FAIL: trigger acceptance contract", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: 100 trigger acceptance cases and reference routes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
