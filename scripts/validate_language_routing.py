#!/usr/bin/env python3
"""Validate the deterministic language-routing contract and cold-start fixtures."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "references" / "language-routing.json"
FIXTURES_PATH = ROOT / "evals" / "language-routing-fixtures.json"
SKILL_PATH = ROOT / "SKILL.md"
MANIFEST_PATH = ROOT / "references" / "locales" / "manifest.json"


def eligible_sessions(case: dict, policy: dict) -> list[dict]:
    minimum_messages = policy["recent_history"]["eligible_min_user_messages"]
    minimum_confidence = policy["auto_learning"]["minimum_confidence"]
    sessions = case.get("recent_sessions", [])
    eligible = [
        session
        for session in sessions
        if isinstance(session, dict)
        and session.get("complete") is True
        and isinstance(session.get("language"), str)
        and session["language"].strip()
        and session.get("user_message_count", 0) >= minimum_messages
        and session.get("confidence") == minimum_confidence
    ]
    return eligible[: policy["recent_history"]["max_sessions"]]


def weighted_recent_language(sessions: list[dict], weights: list[int]) -> str | None:
    usable = [(session["language"], weights[index]) for index, session in enumerate(sessions)]
    if not usable:
        return None
    totals = Counter()
    for language, weight in usable:
        totals[language] += weight
    winner, winner_weight = totals.most_common(1)[0]
    total_weight = sum(totals.values())
    if winner_weight * 2 <= total_weight:
        return None
    return winner


def resolve(case: dict, policy: dict) -> dict:
    slash_aliases = {alias.casefold() for alias in policy.get("slash_only_invocations", [])}
    slash_only = str(case.get("invocation", "")).strip().casefold() in slash_aliases
    available_capabilities = set(case.get("available_capabilities", policy["optional_capabilities"]))
    recent_for_learning = eligible_sessions(case, policy)
    explicit = case.get("explicit_language")
    if explicit:
        locale = explicit
        source = "explicit_current"
    elif case.get("current_message_language"):
        locale = case["current_message_language"]
        source = "current_message"
    else:
        recent = (
            recent_for_learning
            if slash_only and "recent_user_language_signals" in available_capabilities
            else []
        )
        locale = weighted_recent_language(recent, policy["recent_history"]["weights"])
        source = "recent_sessions" if locale else None
        if not locale and case.get("identity_language") and "identity_language_read" in available_capabilities:
            locale = case["identity_language"]
            source = "identity_memory"
        if not locale and case.get("host_locale") and "host_locale" in available_capabilities:
            locale = case["host_locale"]
            source = "host_locale"
    if locale:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        supported = {entry["id"] for entry in manifest.get("locales", [])}
        if locale not in supported:
            locale = manifest.get("fallback_locale", "en")
            source = "fallback_locale"
    result = {
        "locale": locale,
        "source": source or "confirmation",
        "route": "render" if locale else "language_confirmation",
    }
    counts = Counter(session["language"] for session in recent_for_learning)
    learning_locale = weighted_recent_language(
        recent_for_learning, policy["recent_history"]["weights"]
    )
    if case.get("persistence_request") and "identity_language_write" in available_capabilities:
        result["write_locale"] = locale
    elif (
        learning_locale
        and len(recent_for_learning) == policy["auto_learning"]["window_sessions"]
        and counts[learning_locale] >= policy["auto_learning"]["matching_sessions"]
        and "identity_language_write" in available_capabilities
    ):
        result["write_locale"] = learning_locale
    else:
        result["write_locale"] = None
    if "target_market" in case:
        result["target_market"] = case["target_market"]
    return result


def validate_rendering_contract(policy: dict) -> list[str]:
    errors: list[str] = []
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("progressive_resources", {}).get("language_routing") != "references/language-routing.json":
        errors.append("manifest does not route through the language policy resource")
    expected_priority = [
        "explicit_current_language",
        "current_message_language",
        "recent_user_language_signals",
        "identity_language_read",
        "host_locale",
        "language_confirmation",
    ]
    if manifest.get("routing", {}).get("locale_selection_order") != expected_priority:
        errors.append("manifest locale-selection order is incorrect")
    policy_priority = [
        "explicit_current_language",
        "current_message_language",
        "recent_user_language_signals",
        "identity_language_read",
        "host_locale",
        "language_confirmation",
    ]
    if policy.get("priority") != policy_priority:
        errors.append("language policy priority drifted from the manifest contract")
    if not policy.get("slash_only_invocations"):
        errors.append("language policy does not declare exact slash-only invocations")
    locale_resources = manifest.get("locale_progressive_resources", {})
    locales = [entry["id"] for entry in manifest.get("locales", [])]
    for locale in locales:
        resources = locale_resources.get(locale, {})
        for stage in ("round_1", "round_2"):
            stage_path = resources.get(stage)
            if not isinstance(stage_path, str):
                errors.append(f"{locale} {stage} resource is not mapped")
                continue
            path = ROOT / stage_path
            if not path.is_file():
                errors.append(f"{locale} {stage} resource is missing")
                continue
            payload = json.loads(path.read_text(encoding="utf-8"))
            if payload.get("locale") != locale or payload.get("stage") != stage:
                errors.append(f"{locale} {stage} resource metadata is incorrect")
            prompt = payload.get("round", {}).get("prompt")
            if not isinstance(prompt, str) or not prompt.strip():
                errors.append(f"{locale} {stage} prompt is missing")
    skill_text = SKILL_PATH.read_text(encoding="utf-8")
    for phrase in (
        "before producing any visible text",
        "language_locked",
        "fixed bilingual language confirmation",
    ):
        if phrase not in skill_text:
            errors.append(f"SKILL.md is missing visible-output guard: {phrase}")
    confirmation = policy.get("language_confirmation", {}).get("prompt")
    if confirmation != "请选择沟通语言 / Choose your language：`中文` / `English` / 直接输入其他语言":
        errors.append("language confirmation text is not fixed")
    return errors


def validate_contract() -> list[str]:
    errors: list[str] = []
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    fixtures = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    if policy.get("optional_capabilities") != [
        "recent_user_language_signals",
        "identity_language_read",
        "identity_language_write",
        "host_locale",
    ]:
        errors.append("optional language capabilities are not in the declared order")
    recent = policy.get("recent_history", {})
    if recent.get("max_sessions") != 5 or recent.get("weights") != [5, 4, 3, 2, 1]:
        errors.append("recent history window or weights do not match the contract")
    learning = policy.get("auto_learning", {})
    if learning.get("window_sessions") != 5 or learning.get("matching_sessions") != 4:
        errors.append("automatic learning threshold does not match the contract")
    if not isinstance(policy.get("language_confirmation", {}).get("prompt"), str):
        errors.append("language confirmation prompt is missing")
    errors.extend(validate_rendering_contract(policy))
    for case in fixtures.get("cases", []):
        actual = resolve(case, policy)
        expected = case.get("expected", {})
        required_keys = {"locale", "source", "route", "write_locale"}
        if not required_keys <= expected.keys():
            errors.append(f"{case.get('id')}: expected must assert locale, source, route, and write_locale")
        for key, value in expected.items():
            if actual.get(key) != value:
                errors.append(f"{case.get('id')}.{key}: expected {value!r}, got {actual.get(key)!r}")
    return errors


def main() -> int:
    errors = validate_contract()
    if errors:
        print("FAIL: language routing contract")
        for error in errors:
            print(f"- {error}")
        return 1
    fixtures = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    print(f"PASS: language routing contract and {len(fixtures['cases'])} cold-start fixtures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
