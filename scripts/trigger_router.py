#!/usr/bin/env python3
"""Reference semantic trigger router for the prompt-driven DJ Skill.

This is a portable contract/evaluation seam, not a host-specific invocation
implementation. Hosts still decide whether to load the Skill; once loaded,
the same signal contract describes the expected internal route.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "references" / "trigger-signals.json"
VALID_LOCALES = {
    "en", "zh-Hans", "zh-Hant", "es", "pt", "fr", "de", "ja", "ko", "ar",
    "ru", "tr", "hi", "id", "vi", "th", "it", "nl", "pl", "uk", "fa", "bn",
    "ur", "ms", "fil", "sw",
}


def load_contract(path: Path = CONTRACT_PATH) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("trigger contract must be an object")
    return value


def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).casefold()
    value = value.replace("–", "-").replace("—", "-").replace("_", " ")
    value = re.sub(r"[\-/]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def phrase_matches(text: str, phrase: str) -> bool:
    normalized_text = normalize(text)
    normalized_phrase = normalize(phrase)
    if not normalized_phrase:
        return False
    # Word boundaries are useful for standalone Latin terms such as `set`,
    # but they break mixed Chinese/Latin phrases when the adjacent Chinese
    # character is itself considered a word character by the regex engine.
    if normalized_phrase.isascii() and re.search(r"[A-Za-z0-9]", normalized_phrase):
        pattern = rf"(?<![\w]){re.escape(normalized_phrase)}(?![\w])"
        return re.search(pattern, normalized_text, flags=re.UNICODE) is not None
    return normalized_phrase in normalized_text


def matched_terms(text: str, terms: list[str]) -> list[str]:
    return list(dict.fromkeys(term for term in terms if phrase_matches(text, term)))


def occurrence_count(text: str, phrase: str) -> int:
    """Count normalized occurrences for bounded, diminishing genre credit."""
    normalized_text = normalize(text)
    normalized_phrase = normalize(phrase)
    if not normalized_phrase:
        return 0
    if normalized_phrase.isascii() and re.search(r"[A-Za-z0-9]", normalized_phrase):
        pattern = rf"(?<![\w]){re.escape(normalized_phrase)}(?![\w])"
        return len(re.findall(pattern, normalized_text, flags=re.UNICODE))
    return normalized_text.count(normalized_phrase)


def matched_genre_terms(text: str, terms: list[str]) -> list[str]:
    hits: list[str] = []
    for term in terms:
        count = occurrence_count(text, term)
        hits.extend([term] * count)
    return hits


def flatten(values: Any) -> list[str]:
    if isinstance(values, list):
        return [item for item in values if isinstance(item, str) and item.strip()]
    return []


def locale_overlay(contract: dict[str, Any], locale: str) -> dict[str, Any]:
    overlays = contract.get("locale_overlays", {})
    if locale not in VALID_LOCALES:
        locale = "en"
    overlay = overlays.get(locale)
    if not isinstance(overlay, dict):
        raise ValueError(f"missing locale overlay: {locale}")
    return overlay


def mode_terms(contract: dict[str, Any], overlay: dict[str, Any]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for mode, labels in contract.get("mode_map", {}).items():
        values: list[str] = []
        if isinstance(labels, dict):
            values.extend(flatten(labels.get("all")))
            values.extend(flatten(labels.get("zh-Hans")))
            values.extend(flatten(labels.get("zh-Hant")))
        local = overlay.get("mode", {}).get(mode) if isinstance(overlay.get("mode"), dict) else None
        values.extend(flatten(local))
        result[mode] = list(dict.fromkeys(values))
    return result


def signal_matches(text: str, locale: str, contract: dict[str, Any]) -> dict[str, Any]:
    overlay = locale_overlay(contract, locale)
    shared = contract.get("shared_signal_terms", {})
    matches: dict[str, Any] = {}
    command_hits = matched_terms(text, flatten(contract.get("command_aliases")))
    if command_hits:
        matches["command"] = command_hits
    mode_hits: dict[str, list[str]] = {}
    for mode, terms in mode_terms(contract, overlay).items():
        hits = matched_terms(text, terms)
        if hits:
            mode_hits[mode] = hits
    if mode_hits:
        matches["mode"] = mode_hits

    for family in ("dj_action", "dj_object", "dj_context", "reference", "set_detail", "generic_music_term", "negative_context", "explanatory_context"):
        terms = flatten(overlay.get(family))
        if family in shared:
            terms.extend(flatten(shared.get(family)))
        if family == "negative_context":
            terms.extend(flatten(contract.get("global_negative_contexts")))
        hits = matched_terms(text, list(dict.fromkeys(terms)))
        if hits:
            matches[family] = hits

    genre_hits: dict[str, list[str]] = {}
    for family, aliases in contract.get("genre_families", {}).items():
        hits = matched_genre_terms(text, flatten(aliases))
        if hits:
            genre_hits[family] = hits
    if genre_hits:
        matches["genre"] = genre_hits

    genre_context = matched_terms(text, flatten(overlay.get("genre_context")) + flatten(shared.get("genre_context")))
    if genre_context:
        matches["genre_context"] = genre_context
    return matches


def score_matches(matches: dict[str, Any], contract: dict[str, Any]) -> tuple[int, dict[str, int]]:
    weights = contract.get("weights", {})
    contributions: dict[str, int] = {}
    score = 0
    if matches.get("command"):
        contributions["command"] = 100
        score += 100
    for family in ("mode", "dj_action", "dj_context", "reference", "set_detail"):
        value = matches.get(family)
        if not value:
            continue
        count = len(value) if isinstance(value, list) else len(value)
        weight = int(weights.get(family, 0))
        contribution = weight if family != "set_detail" else min(weight + (count - 1) * 5, 25)
        contributions[family] = contribution
        score += contribution

    if matches.get("genre_context"):
        contribution = int(weights.get("genre", 0))
        contributions["genre_context"] = contribution
        score += contribution

    if matches.get("dj_object"):
        count = len(matches["dj_object"])
        contribution = int(weights.get("dj_object", 0))
        object_is_only_generic = set(matches.get("dj_object", [])) <= set(matches.get("generic_music_term", []))
        has_context = any(
            matches.get(family)
            for family in ("mode", "dj_action", "dj_context", "genre", "genre_context", "reference")
        )
        if object_is_only_generic and not has_context:
            contribution = 25
        contributions["dj_object"] = contribution
        score += contribution

    families = matches.get("genre", {})
    if families:
        distinct = len(families)
        occurrences = sum(len(values) for values in families.values())
        first = int(weights.get("genre", 0))
        contribution = first
        contribution += min(max(distinct - 1, 0) * int(weights.get("repeated_genre_distinct_family", 0)), 10)
        repeats = max(occurrences - distinct, 0)
        same_family_weight = int(weights.get("repeated_genre_same_family", 0))
        diminishing_repeat_bonus = sum(
            max(1, same_family_weight // (index + 1))
            for index in range(repeats)
        )
        contribution += min(diminishing_repeat_bonus, 6)
        contributions["genre"] = contribution
        score += contribution

    relevant_families = {"dj_action", "dj_object", "dj_context", "genre", "genre_context", "reference", "mode"}
    if len(relevant_families & matches.keys()) >= 2:
        score += int(weights.get("direct_pair_bonus", 0))
        contributions["direct_pair_bonus"] = int(weights.get("direct_pair_bonus", 0))
    return score, contributions


def confidence(score: int, contract: dict[str, Any]) -> str:
    for band in ("very_high", "high", "medium", "low"):
        minimum = int(contract.get("confidence_bands", {}).get(band, {}).get("minimum", 0))
        if score >= minimum:
            return band
    return "low"


def classify(text: str, locale: str = "en", contract: dict[str, Any] | None = None) -> dict[str, Any]:
    contract = contract or load_contract()
    matches = signal_matches(text, locale, contract)
    score, contributions = score_matches(matches, contract)
    hard_negative = bool(matches.get("negative_context"))
    explanatory = bool(matches.get("explanatory_context"))
    mode_only = bool(matches.get("mode")) and not any(
        matches.get(family) for family in ("dj_action", "dj_object", "dj_context", "genre", "genre_context", "reference")
    )
    only_genre = bool(matches.get("genre") or matches.get("genre_context")) and not any(
        matches.get(family) for family in ("mode", "dj_action", "dj_object", "dj_context", "reference")
    )
    generic_only = bool(matches.get("generic_music_term")) and not any(
        matches.get(family) for family in ("mode", "dj_action", "dj_context", "genre", "genre_context", "reference")
    )
    specific_object = bool(matches.get("dj_object")) and any(
        object_term not in set(matches.get("generic_music_term", []))
        for object_term in matches["dj_object"]
    )
    reference_without_dj_intent = bool(matches.get("reference")) and not any(
        matches.get(family) for family in ("mode", "dj_action", "dj_object", "dj_context")
    )
    direct_combinations = contract.get("route_rules", {}).get("direct_combinations", [])
    direct_pair = any(
        isinstance(pair, list) and set(pair) <= set(matches)
        for pair in direct_combinations
    )
    # Keep explicit non-English action phrases such as 挖歌/排set useful,
    # while bare English discovery verbs (find/dig/digging) remain ambiguous.
    action_hits = set(matches.get("dj_action", []))
    weak_action_hits = {"find", "dig", "digging"}
    strong_action_only = bool(action_hits) and not action_hits <= weak_action_hits
    has_music_signal = bool(matches)
    route = "non_trigger"
    if hard_negative or (explanatory and (mode_only or only_genre or "genre" in matches or "genre_context" in matches)):
        route = "non_trigger"
    elif reference_without_dj_intent or mode_only or only_genre:
        route = "non_trigger"
    elif generic_only and not specific_object:
        route = "ambiguous_confirmation"
    elif matches.get("command") or specific_object or direct_pair or (
        strong_action_only and score >= int(contract.get("route_rules", {}).get("direct_score_threshold", 70))
    ):
        route = "direct"
    elif has_music_signal and score >= int(contract.get("route_rules", {}).get("ambiguous_score_threshold", 25)):
        route = "ambiguous_confirmation"

    if route == "direct":
        host_invocation = "must_invoke"
    elif route == "ambiguous_confirmation":
        host_invocation = "must_invoke"
    else:
        host_invocation = "must_not_invoke"

    return {
        "locale": locale if locale in VALID_LOCALES else "en",
        "host_invocation": host_invocation,
        "skill_route": route,
        "score": score,
        "confidence": confidence(score, contract),
        "matches": matches,
        "contributions": contributions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify a DJ Skill trigger request")
    parser.add_argument("text")
    parser.add_argument("--locale", default="en")
    args = parser.parse_args()
    try:
        print(json.dumps(classify(args.text, args.locale), ensure_ascii=False, indent=2))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
