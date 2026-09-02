#!/usr/bin/env python3
"""Validate the fixed multilingual contract used by dj-crate-digger.

Locale packs are Markdown files with one machine-readable JSON block.  The
validator intentionally checks shape and routing rules rather than attempting
to judge translation quality.  It is a regression contract for a prompt-driven
Skill, not a runtime locale resolver.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import validate_language_routing
import validate_trigger_acceptance
import trigger_router


ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "references" / "locales"
MANIFEST_PATH = LOCALES_DIR / "manifest.json"
FIXTURE_PATH = ROOT / "evals" / "locale-contract-fixtures.json"
MULTILINGUAL_EVAL_PATH = ROOT / "evals" / "multilingual-evals.json"
TRIGGER_EVAL_PATH = ROOT / "evals" / "trigger-evals.json"
LEGACY_TRIGGER_EVAL_PATH = ROOT / "evals" / "trigger-regression-legacy.json"
TRIGGER_SIGNAL_PATH = ROOT / "references" / "trigger-signals.json"
INTAKE_FIXTURE_PATH = ROOT / "evals" / "intake-template-fixtures.json"

EXPECTED_LOCALES = (
    "en",
    "zh-Hans",
    "zh-Hant",
    "es",
    "pt",
    "fr",
    "de",
    "ja",
    "ko",
    "ar",
    "ru",
    "tr",
    "hi",
    "id",
    "vi",
    "th",
    "it",
    "nl",
    "pl",
    "uk",
    "fa",
    "bn",
    "ur",
    "ms",
    "fil",
    "sw",
)
EXPECTED_LOCALE_SELECTION_ORDER = (
    "explicit_current_language",
    "current_message_language",
    "recent_user_language_signals",
    "identity_language_read",
    "host_locale",
    "language_confirmation",
)
EXPECTED_GLOBAL_MARKETS = (
    ("mainland-china", "zh-Hans", "Mainland China", "NetEase Cloud Music"),
    ("united-kingdom", "en", "United Kingdom", "SoundCloud, Bandcamp, Beatport"),
    ("japan", "ja", "Japan", "Apple Music"),
    ("germany", "de", "Germany", "Spotify"),
    ("brazil", "pt", "Brazil", "Spotify, SoundCloud"),
    ("south-korea", "ko", "South Korea", "Apple Music, Spotify"),
)
REQUIRED_PROGRESSIVE_RESOURCES = (
    "language_routing",
    "preflight",
    "trigger_signals",
    "trigger",
    "intake",
    "search",
    "ranking",
    "deduplication",
    "key_and_sequencing",
    "feedback_memory",
    "export",
    "mode_fast",
    "mode_brief",
    "mode_rich",
    "report",
)
FIRST_FIELDS = (
    "scene",
    "target_market",
    "core_sound",
    "track_count_or_duration",
    "output_mode",
    "other",
)
SECOND_FIELDS = (
    "style",
    "bpm",
    "familiarity_era",
    "era_classic",
    "mood",
    "energy",
    "platform",
    "other",
)
ACTION_INTENTS = (
    "share_feedback",
    "export_w4dj",
    "output_text_playlist",
    "harmonic_reorder",
    "confirm_long_term_memory",
)
TRIGGER_CAPSULE_MINIMUM = 4
REQUIRED_LOCALE_STAGE_KEYS = (
    "trigger",
    "round_1",
    "round_2",
    "search_context",
    "report_fast",
    "report_brief",
    "report_rich",
    "post_report",
    "capability_errors",
)
REPORT_MODES = ("fast", "brief", "rich")
REQUIRED_STATUS_KEYS = (
    "unknown",
    "verified",
    "target_platform_missing",
)
TRIGGER_SIGNAL_KEYS = (
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
    "genre_families",
)
TRIGGER_GENRE_FAMILIES = (
    "house",
    "disco",
    "techno",
    "dubstep",
    "bass",
    "drum_and_bass",
    "breakbeat",
    "jungle",
    "garage",
    "trance",
    "psytrance",
    "progressive",
    "electro",
    "future_bass",
    "big_room",
    "hard_dance",
    "hardcore",
    "melodic_techno",
)
FIXED_CHINESE_LEAKS = (
    "场景：",
    "目标国家 / 地区：",
    "核心声音方向：",
    "选歌碎碎念",
    "下一步",
    "导出到w4dj",
    "输出文字版歌单",
    "需要我根据五度圈",
)
JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)


def load_pack(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    matches = JSON_FENCE_RE.findall(text)
    if len(matches) != 1 or text.count("```") != 2:
        raise ValueError(f"{path.name}: expected exactly one JSON code block")
    try:
        value = json.loads(matches[0])
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path.name}: invalid JSON block: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path.name}: JSON block must contain an object")
    # Chinese packs intentionally contain the migrated Chinese UI contract;
    # non-Chinese packs must not accidentally fall back to those labels.
    try:
        pack_locale = json.loads(matches[0]).get("locale")
    except json.JSONDecodeError:
        pack_locale = None
    if not (isinstance(pack_locale, str) and pack_locale.startswith("zh-")) and any(
        phrase in text for phrase in FIXED_CHINESE_LEAKS
    ):
        raise ValueError(f"{path.name}: fixed Chinese UI text leaked into locale pack")
    return value


def require_text(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: expected non-empty text")


def require_string_list(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        errors.append(f"{label}: expected a non-empty string list")


def validate_trigger_signal_contract() -> tuple[dict[str, Any] | None, list[str]]:
    """Validate the central semantic trigger contract before its projections."""
    errors: list[str] = []
    if not TRIGGER_SIGNAL_PATH.exists():
        return None, [f"missing central trigger contract: {TRIGGER_SIGNAL_PATH}"]
    try:
        contract = json.loads(TRIGGER_SIGNAL_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"central trigger contract is not valid JSON: {exc}"]
    if not isinstance(contract, dict):
        return None, ["central trigger contract must contain an object"]
    if contract.get("schema") != "dj-crate-digger-trigger-signals":
        errors.append("central trigger contract has an unexpected schema")
    if contract.get("version") != 1:
        errors.append("central trigger contract version must be 1")
    expected_signal_families = (
        "mode",
        "dj_action",
        "dj_object",
        "dj_context",
        "genre",
        "reference",
        "set_detail",
        "negative_context",
    )
    if tuple(contract.get("signal_families", ())) != expected_signal_families:
        errors.append("central trigger contract signal_families are incomplete or out of order")
    require_string_list(contract.get("command_aliases"), "command_aliases", errors)
    normalization = contract.get("normalization")
    if not isinstance(normalization, dict):
        errors.append("central trigger contract is missing normalization")
    else:
        if normalization.get("unicode") != "NFKC" or normalization.get("casefold") is not True:
            errors.append("central trigger contract normalization must use NFKC and casefold")
        if not isinstance(normalization.get("separator_equivalences"), list):
            errors.append("central trigger contract must declare separator equivalences")

    expected_weights = {
        "mode": 100,
        "dj_action": 70,
        "dj_object": 60,
        "dj_context": 45,
        "genre": 35,
        "reference": 35,
        "set_detail": 15,
    }
    weights = contract.get("weights")
    if not isinstance(weights, dict):
        errors.append("central trigger contract is missing weights")
    else:
        for key, expected in expected_weights.items():
            if weights.get(key) != expected:
                errors.append(f"central trigger contract weight {key!r} must be {expected}")
        for key in ("repeated_genre_same_family", "repeated_genre_distinct_family", "direct_pair_bonus"):
            if not isinstance(weights.get(key), int) or weights[key] < 0:
                errors.append(f"central trigger contract weight {key!r} must be a non-negative integer")

    bands = contract.get("confidence_bands")
    if not isinstance(bands, dict) or tuple(bands) != ("very_high", "high", "medium", "low"):
        errors.append("central trigger contract confidence bands are incomplete or out of order")
    else:
        thresholds = [bands[name].get("minimum") for name in bands if isinstance(bands[name], dict)]
        if thresholds != sorted(thresholds, reverse=True):
            errors.append("central trigger contract confidence bands must descend in threshold order")

    route_rules = contract.get("route_rules")
    if not isinstance(route_rules, dict):
        errors.append("central trigger contract is missing route_rules")
    else:
        required_rules = {
            "hard_negative_first",
            "direct_score_threshold",
            "ambiguous_score_threshold",
            "style_only_is_non_trigger",
            "generic_only_is_ambiguous",
            "direct_combinations",
        }
        if not required_rules <= set(route_rules):
            errors.append("central trigger contract route_rules are incomplete")
        if route_rules.get("hard_negative_first") is not True:
            errors.append("central trigger contract must enable hard negative precedence")

    mode_map = contract.get("mode_map")
    if not isinstance(mode_map, dict) or set(mode_map) != {"fast", "composite", "four_views"}:
        errors.append("central trigger contract mode_map must define fast, composite, and four_views")
    else:
        for mode, labels in mode_map.items():
            if not isinstance(labels, dict) or not isinstance(labels.get("all"), list):
                errors.append(f"central trigger contract mode_map.{mode} must include an all list")
            elif not labels["all"]:
                errors.append(f"central trigger contract mode_map.{mode}.all must not be empty")

    genre_families = contract.get("genre_families")
    if not isinstance(genre_families, dict) or tuple(genre_families) != TRIGGER_GENRE_FAMILIES:
        errors.append("central trigger contract genre families do not match the supported electronic family set")
    else:
        for family, aliases in genre_families.items():
            require_string_list(aliases, f"genre_families.{family}", errors)

    shared = contract.get("shared_signal_terms")
    if not isinstance(shared, dict):
        errors.append("central trigger contract is missing shared signal terms")
    else:
        for family in ("dj_context", "reference", "set_detail", "genre_context"):
            require_string_list(shared.get(family), f"shared_signal_terms.{family}", errors)
    require_string_list(contract.get("global_negative_contexts"), "global_negative_contexts", errors)

    overlays = contract.get("locale_overlays")
    if not isinstance(overlays, dict) or tuple(overlays) != EXPECTED_LOCALES:
        errors.append("central trigger contract locale overlays do not match the 26-locale manifest")
    else:
        for locale, overlay in overlays.items():
            if not isinstance(overlay, dict):
                errors.append(f"central trigger contract overlay {locale} must be an object")
                continue
            for family in ("dj_action", "dj_object", "dj_context", "reference", "set_detail", "generic_music_term", "negative_context", "explanatory_context"):
                require_string_list(overlay.get(family), f"locale_overlays.{locale}.{family}", errors)
            modes = overlay.get("mode")
            if not isinstance(modes, dict) or set(modes) != {"fast", "composite", "four_views"}:
                errors.append(f"locale_overlays.{locale}.mode must define all three modes")
            else:
                for mode in ("fast", "composite", "four_views"):
                    require_string_list(modes.get(mode), f"locale_overlays.{locale}.mode.{mode}", errors)
    return contract, errors


def expected_semantic_projection(contract: dict[str, Any], locale: str) -> dict[str, Any]:
    overlay = contract["locale_overlays"][locale]
    shared = contract["shared_signal_terms"]
    projected: dict[str, Any] = {}
    for key in TRIGGER_SIGNAL_KEYS:
        if key == "genre_families":
            projected[key] = list(contract["genre_families"])
        elif key in overlay:
            projected[key] = overlay[key]
        elif key == "genre_context":
            projected[key] = shared.get(key, [])
        else:
            projected[key] = []
    return projected


def validate_round(
    pack: dict[str, Any], round_key: str, expected_fields: tuple[str, ...]
) -> list[str]:
    errors: list[str] = []
    round_data = pack.get("intake", {}).get(round_key)
    if not isinstance(round_data, dict):
        return [f"{pack.get('locale', '?')} {round_key}: missing object"]

    require_text(round_data.get("title"), f"{round_key}.title", errors)
    rules = round_data.get("rules")
    require_string_list(rules, f"{round_key}.rules", errors)
    expected_rule_count = 2 if round_key == "round_1" else 1
    if isinstance(rules, list) and len(rules) != expected_rule_count:
        errors.append(
            f"{round_key}.rules: expected {expected_rule_count} fixed rule(s), got {len(rules)}"
        )
    fields = round_data.get("fields")
    if not isinstance(fields, list):
        return errors + [f"{round_key}.fields: expected list"]
    actual_keys = tuple(
        item.get("key") for item in fields if isinstance(item, dict)
    )
    if actual_keys != expected_fields:
        errors.append(
            f"{round_key}.fields: expected {expected_fields!r}, got {actual_keys!r}"
        )
    for index, field in enumerate(fields):
        if not isinstance(field, dict):
            errors.append(f"{round_key}.fields[{index}]: expected object")
            continue
        require_text(field.get("label"), f"{round_key}.fields[{index}].label", errors)
        if field.get("key") == "other":
            if not isinstance(field.get("example"), str):
                errors.append(f"{round_key}.fields[{index}].example: expected text")
        else:
            require_text(field.get("example"), f"{round_key}.fields[{index}].example", errors)

    prompt = round_data.get("prompt")
    require_text(prompt, f"{round_key}.prompt", errors)
    if isinstance(prompt, str):
        if len(re.findall(r"^```markdown$", prompt, flags=re.MULTILINE)) != 1 or len(
            re.findall(r"^```$", prompt, flags=re.MULTILINE)
        ) != 1:
            errors.append(
                f"{round_key}.prompt: expected exactly one fenced Markdown fill-in block"
            )
        if any(field.get("label") not in prompt for field in fields if isinstance(field, dict)):
            errors.append(f"{round_key}.prompt: one or more field labels are absent")
    return errors


def validate_report(pack: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    report = pack.get("report")
    if not isinstance(report, dict):
        return [f"{pack.get('locale', '?')}: missing report object"]
    expected_columns = {"fast": 3, "brief": 12, "rich": 12}
    for mode in REPORT_MODES:
        data = report.get(mode)
        if not isinstance(data, dict):
            errors.append(f"{pack.get('locale', '?')} report.{mode}: missing object")
            continue
        require_text(data.get("title"), f"report.{mode}.title", errors)
        require_text(data.get("first_batch_title"), f"report.{mode}.first_batch_title", errors)
        require_text(data.get("final_title"), f"report.{mode}.final_title", errors)
        columns = data.get("columns")
        if not isinstance(columns, list) or len(columns) != expected_columns[mode]:
            errors.append(
                f"report.{mode}.columns: expected {expected_columns[mode]} items"
            )
        elif not all(isinstance(column, str) and column.strip() for column in columns):
            errors.append(f"report.{mode}.columns: all labels must be non-empty text")
        next_steps = data.get("next_steps")
        expected_steps = 2 if mode == "fast" else 3
        if not isinstance(next_steps, list) or len(next_steps) != expected_steps:
            errors.append(
                f"report.{mode}.next_steps: expected {expected_steps} items"
            )
        elif not all(
            isinstance(step, dict)
            and isinstance(step.get("label"), str)
            and step["label"].strip()
            and isinstance(step.get("body"), str)
            and step["body"].strip()
            for step in next_steps
        ):
            errors.append(f"report.{mode}.next_steps: malformed step")
        else:
            handoff_body = next_steps[1]["body"]
            if "W4DJ" not in handoff_body:
                errors.append(
                    f"report.{mode}.next_steps[1].body: must retain the W4DJ handoff"
                )
            if pack.get("locale") == "zh-Hans":
                if "输出文字版歌单" not in handoff_body:
                    errors.append(
                        f"report.{mode}.next_steps[1].body: must retain the text-playlist action"
                    )
                if mode != "fast" and "五度圈" not in next_steps[2]["body"]:
                    errors.append(
                        f"report.{mode}.next_steps[2].body: must retain the harmonic-order action"
                    )
        for label_key in (
            "digging_notes",
            "mix_suggestion",
            "unknown",
            "verified",
            "target_platform_missing",
        ):
            require_text(data.get(label_key), f"report.{mode}.{label_key}", errors)
    rich = report.get("rich")
    if isinstance(rich, dict):
        view_titles = rich.get("view_titles")
        if not isinstance(view_titles, list) or len(view_titles) != 4:
            errors.append("report.rich.view_titles: expected four view titles")
    return errors


def validate_actions(pack: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    actions = pack.get("actions")
    if not isinstance(actions, dict):
        return [f"{pack.get('locale', '?')}: missing actions object"]
    for intent in ACTION_INTENTS:
        data = actions.get(intent)
        if not isinstance(data, dict):
            errors.append(f"{pack.get('locale', '?')} actions.{intent}: missing object")
            continue
        require_text(data.get("label"), f"actions.{intent}.label", errors)
        for expression_kind in ("positive", "negative", "ambiguous"):
            require_string_list(
                data.get(expression_kind),
                f"actions.{intent}.{expression_kind}",
                errors,
            )
    return errors


def validate_pack(pack: dict[str, Any], expected_locale: str) -> list[str]:
    errors: list[str] = []
    locale = pack.get("locale")
    if locale != expected_locale:
        errors.append(f"{expected_locale}: pack locale is {locale!r}")
    for key in ("language_name", "native_name", "direction"):
        require_text(pack.get(key), f"{expected_locale}.{key}", errors)
    if pack.get("direction") not in ("ltr", "rtl"):
        errors.append(f"{expected_locale}.direction: expected ltr or rtl")

    trigger_capsule = pack.get("trigger_capsule")
    if (
        not isinstance(trigger_capsule, list)
        or len(trigger_capsule) < TRIGGER_CAPSULE_MINIMUM
        or not all(isinstance(item, str) and item.strip() for item in trigger_capsule)
    ):
        errors.append(
            f"{expected_locale}.trigger_capsule: expected at least {TRIGGER_CAPSULE_MINIMUM} localized DJ triggers"
        )

    market_policy = pack.get("market_policy")
    if not isinstance(market_policy, dict):
        errors.append(f"{expected_locale}: missing market_policy")
    else:
        if market_policy.get("language_independent") is not True:
            errors.append(f"{expected_locale}: language/market separation is not enabled")
        for key in ("blank_region", "explicit_region", "persistence"):
            require_text(market_policy.get(key), f"{expected_locale}.market_policy.{key}", errors)

    quick_start = pack.get("quick_start")
    if not isinstance(quick_start, dict):
        errors.append(f"{expected_locale}: missing quick_start")
    else:
        for key in ("intro", "tutorial_label", "tutorial_url"):
            require_text(quick_start.get(key), f"{expected_locale}.quick_start.{key}", errors)
        expected_tutorial = (
            "/docs/w4dj/README.md"
            if expected_locale.startswith("zh-")
            else "/docs/w4dj/README.en.md"
        )
        if expected_tutorial not in str(quick_start.get("tutorial_url", "")):
            errors.append(f"{expected_locale}: tutorial URL must use {expected_tutorial}")

    errors.extend(validate_round(pack, "round_1", FIRST_FIELDS))
    errors.extend(validate_round(pack, "round_2", SECOND_FIELDS))
    errors.extend(validate_report(pack))
    errors.extend(validate_actions(pack))

    status = pack.get("status")
    if not isinstance(status, dict):
        errors.append(f"{expected_locale}: missing status object")
    else:
        for key in REQUIRED_STATUS_KEYS:
            require_text(status.get(key), f"{expected_locale}.status.{key}", errors)

    platform_policy = pack.get("platform_policy")
    if not isinstance(platform_policy, dict):
        errors.append(f"{expected_locale}: missing platform_policy")
    else:
        aliases = platform_policy.get("aliases")
        if not isinstance(aliases, dict) or len(aliases) < 7:
            errors.append(f"{expected_locale}.platform_policy.aliases: expected at least 7 platforms")
        for key in ("exclusive_markers", "preferred_markers", "fallback_markers", "forbidden_markers"):
            require_string_list(
                platform_policy.get(key),
                f"{expected_locale}.platform_policy.{key}",
                errors,
            )

    export = pack.get("export")
    if not isinstance(export, dict):
        errors.append(f"{expected_locale}: missing export object")
    else:
        for key in ("text", "w4dj", "harmonic", "feedback", "memory_confirmation"):
            require_text(export.get(key), f"{expected_locale}.export.{key}", errors)
    serialized = json.dumps(pack, ensure_ascii=False).lower()
    retired_tokens = (
        "v1",
        "v2",
        "format_" + "version",
        "." + "t" + "x" + "t",
        "." + "w4djcrate",
        "m" + "3u8",
    )
    for token in retired_tokens:
        if token in serialized:
            errors.append(f"{expected_locale}: locale pack contains retired token {token!r}")
    return errors


def validate_manifest() -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    if not MANIFEST_PATH.exists():
        return None, [f"missing locale manifest: {MANIFEST_PATH}"]
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [f"manifest is not valid JSON: {exc}"]
    if not isinstance(manifest, dict):
        return None, ["manifest must contain an object"]
    if manifest.get("default_locale") != "en" or manifest.get("fallback_locale") != "en":
        errors.append("manifest: default_locale and fallback_locale must both be en")
    routing = manifest.get("routing")
    if not isinstance(routing, dict) or tuple(
        routing.get("locale_selection_order", [])
    ) != EXPECTED_LOCALE_SELECTION_ORDER:
        errors.append("manifest.routing: locale selection order is incomplete or changed")
    progressive_resources = manifest.get("progressive_resources")
    if not isinstance(progressive_resources, dict):
        errors.append("manifest.progressive_resources: missing resource map")
    else:
        for key in REQUIRED_PROGRESSIVE_RESOURCES:
            resource = progressive_resources.get(key)
            if not isinstance(resource, str) or not (ROOT / resource).exists():
                errors.append(f"manifest.progressive_resources: missing {key}")
    locale_progressive = manifest.get("locale_progressive_resources")
    if not isinstance(locale_progressive, dict):
        errors.append("manifest.locale_progressive_resources: missing resource map")
    else:
        if tuple(locale_progressive) != EXPECTED_LOCALES:
            errors.append("manifest.locale_progressive_resources: locale order does not match manifest")
        for locale in EXPECTED_LOCALES:
            mapping = locale_progressive.get(locale)
            if not isinstance(mapping, dict):
                errors.append(f"manifest.locale_progressive_resources: missing {locale}")
                continue
            if set(mapping) != set(REQUIRED_LOCALE_STAGE_KEYS):
                errors.append(f"manifest.locale_progressive_resources.{locale}: stage keys are incomplete")
            for stage in REQUIRED_LOCALE_STAGE_KEYS:
                resource = mapping.get(stage)
                if not isinstance(resource, str):
                    errors.append(f"manifest.locale_progressive_resources.{locale}: missing {stage}")
                    continue
                path = ROOT / resource
                if not path.exists():
                    errors.append(f"manifest.locale_progressive_resources.{locale}: missing file {resource}")
                    continue
                try:
                    payload = json.loads(path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    errors.append(f"{resource}: invalid JSON: {exc}")
                    continue
                if payload.get("locale") != locale or payload.get("stage") != stage:
                    errors.append(f"{resource}: locale/stage metadata mismatch")
                if stage in ("round_1", "round_2") and not isinstance(payload.get("round"), dict):
                    errors.append(f"{resource}: missing round payload")
                if stage.startswith("report_") and not isinstance(payload.get("report"), dict):
                    errors.append(f"{resource}: missing report payload")
                if stage == "trigger":
                    if not isinstance(payload.get("ambiguous_confirmation"), str):
                        errors.append(f"{resource}: missing ambiguous confirmation")
                    readiness_choice = payload.get("readiness_choice")
                    if not isinstance(readiness_choice, str) or not readiness_choice.strip():
                        errors.append(f"{resource}: missing readiness choice")
                    elif "1" not in readiness_choice or "2" not in readiness_choice:
                        errors.append(f"{resource}: readiness choice must expose options 1 and 2")
                    for trigger_kind in ("direct", "ambiguous", "non_trigger"):
                        require_string_list(
                            payload.get(trigger_kind),
                            f"{resource}.{trigger_kind}",
                            errors,
                        )
                    direct = set(payload.get("direct", []))
                    ambiguous = set(payload.get("ambiguous", []))
                    overlap = sorted(direct & ambiguous)
                    if overlap:
                        errors.append(f"{resource}: direct and ambiguous triggers overlap: {overlap!r}")
                    for cue in direct:
                        if trigger_router.classify(cue, locale).get("skill_route") != "direct":
                            errors.append(f"{resource}: direct cue does not resolve to direct: {cue!r}")
                    for cue in ambiguous:
                        if trigger_router.classify(cue, locale).get("skill_route") != "ambiguous_confirmation":
                            errors.append(f"{resource}: ambiguous cue does not resolve to ambiguous_confirmation: {cue!r}")
                if stage == "search_context" and not isinstance(payload.get("platform_policy"), dict):
                    errors.append(f"{resource}: missing platform policy")
                if stage == "post_report" and not isinstance(payload.get("actions"), dict):
                    errors.append(f"{resource}: missing post-report actions")
                if stage == "capability_errors" and not isinstance(payload.get("messages"), dict):
                    errors.append(f"{resource}: missing capability messages")
    entries = manifest.get("locales")
    if not isinstance(entries, list):
        return manifest, errors + ["manifest.locales must be a list"]
    ids = tuple(entry.get("id") for entry in entries if isinstance(entry, dict))
    if ids != EXPECTED_LOCALES:
        errors.append(f"manifest.locales: expected {EXPECTED_LOCALES!r}, got {ids!r}")
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("manifest.locales: every entry must be an object")
            continue
        locale = entry.get("id")
        filename = entry.get("file")
        if locale not in EXPECTED_LOCALES:
            errors.append(f"manifest: unexpected locale {locale!r}")
        if not isinstance(filename, str) or Path(filename).name != filename:
            errors.append(f"manifest {locale!r}: file must be a simple filename")
        elif not (LOCALES_DIR / filename).exists():
            errors.append(f"manifest {locale!r}: missing file {filename}")
    return manifest, errors


def validate_trigger_projections(
    contract: dict[str, Any] | None, manifest: dict[str, Any] | None
) -> list[str]:
    """Ensure stage JSON and full locale packs are projections of one source."""
    if contract is None or manifest is None:
        return []
    errors: list[str] = []
    expected_contract_ref = {"path": "references/trigger-signals.json", "version": contract.get("version")}
    expected_families = list(TRIGGER_SIGNAL_KEYS)
    for entry in manifest.get("locales", []):
        if not isinstance(entry, dict):
            continue
        locale = entry.get("id")
        if locale not in EXPECTED_LOCALES:
            continue
        stage_path = ROOT / manifest["locale_progressive_resources"][locale]["trigger"]
        try:
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
        except (OSError, KeyError, json.JSONDecodeError) as exc:
            errors.append(f"{locale}: cannot load trigger projection: {exc}")
            continue
        if stage.get("trigger_contract") != expected_contract_ref:
            errors.append(f"{stage_path}: trigger_contract does not reference the central contract")
        if stage.get("semantic_signals") != expected_semantic_projection(contract, locale):
            errors.append(f"{stage_path}: semantic_signals drifted from the central locale overlay")

        locale_path = LOCALES_DIR / entry["file"]
        try:
            pack = load_pack(locale_path)
        except (OSError, ValueError) as exc:
            errors.append(f"{locale_path}: cannot load trigger projection: {exc}")
            continue
        if pack.get("trigger_contract") != expected_contract_ref:
            errors.append(f"{locale_path}: trigger_contract does not reference the central contract")
        if pack.get("trigger_signal_families") != expected_families:
            errors.append(f"{locale_path}: trigger_signal_families drifted from the stage contract")
    return errors


def validate_fixtures() -> list[str]:
    if not FIXTURE_PATH.exists():
        return [f"missing locale fixtures: {FIXTURE_PATH}"]
    try:
        fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"locale fixtures are not valid JSON: {exc}"]
    if not isinstance(fixtures, dict):
        return ["locale fixtures must contain an object"]
    errors: list[str] = []
    for key in ("language_market_cases", "action_cases", "platform_cases"):
        value = fixtures.get(key)
        if not isinstance(value, list) or not value:
            errors.append(f"locale fixtures: {key} must be a non-empty list")
    expected_market_cases = {
        "english-explicit-japan": ("en", "Japan", "user_provided", False),
        "spanish-explicit-mexico": ("es", "Mexico", "user_provided", False),
        "arabic-explicit-uk": ("ar", "United Kingdom", "user_provided", False),
        "blank-language-market": ("en", "broad English-language market", "language_inferred", False),
    }
    market_cases = {
        case.get("name"): case
        for case in fixtures.get("language_market_cases", [])
        if isinstance(case, dict)
    }
    for name, expected in expected_market_cases.items():
        case = market_cases.get(name)
        if case is None or tuple(
            case.get(key)
            for key in ("communication_language", "target_market", "target_market_source", "persist_target_market")
        ) != expected:
            errors.append(f"locale fixtures: invalid language/market case {name!r}")
    return errors


def validate_action_fixtures() -> list[str]:
    """Ensure representative localized phrases resolve to their declared intent."""
    if not FIXTURE_PATH.exists():
        return []
    fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    for case in fixtures.get("action_cases", []):
        locale = str(case.get("locale"))
        intent = str(case.get("intent"))
        kind = str(case.get("kind"))
        try:
            manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            post_report = manifest["locale_progressive_resources"][locale]["post_report"]
            payload = json.loads((ROOT / post_report).read_text(encoding="utf-8"))
            expressions = payload["actions"][intent][kind]
        except (OSError, KeyError, TypeError, ValueError) as exc:
            errors.append(f"action fixture {case.get('input', '<missing>')!r}: {exc}")
            continue
        if case.get("input") not in expressions:
            errors.append(
                f"action fixture {case.get('input')!r}: phrase is not declared for "
                f"{locale}.{intent}.{kind}"
            )
    return errors


def validate_multilingual_eval_spec() -> list[str]:
    """Validate the declared acceptance matrix without faking model replays."""
    if not MULTILINGUAL_EVAL_PATH.exists():
        return [f"missing multilingual eval specification: {MULTILINGUAL_EVAL_PATH}"]
    try:
        spec = json.loads(MULTILINGUAL_EVAL_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"multilingual eval specification is not valid JSON: {exc}"]
    if not isinstance(spec, dict):
        return ["multilingual eval specification must contain an object"]

    errors: list[str] = []
    if tuple(spec.get("locales", [])) != EXPECTED_LOCALES:
        errors.append("multilingual eval locales do not match the 26-locale manifest")

    expected_case_ids = {
        "slash-cold-start-language",
        "language-market-separation",
        "fixed-intake-template",
        "adaptive-intake-routing",
        "report-shape",
        "localized-action-intents",
        "localized-platform-policy",
        "localized-exports-and-harmonic-order",
    }
    cases = spec.get("static_cases")
    actual_case_ids = {
        case.get("id") for case in cases if isinstance(case, dict)
    } if isinstance(cases, list) else set()
    if actual_case_ids != expected_case_ids:
        errors.append("multilingual eval static cases are incomplete or unexpected")

    replay = spec.get("model_replay")
    if not isinstance(replay, dict):
        return errors + ["multilingual eval model_replay must contain an object"]
    if replay.get("required_runs") != len(EXPECTED_LOCALES) * 6 * 2:
        errors.append("multilingual eval required_runs must equal 312")
    expected_flows = (
        "complete-one-message",
        "delegated-one-message",
        "underspecified-intake",
        "slash-language-cold-start",
        "explicit-fast",
        "explicit-rich",
    )
    if tuple(replay.get("flows", [])) != expected_flows:
        errors.append("multilingual eval cold-start flows do not match the adaptive intake contract")
    if tuple(replay.get("model_profiles", [])) != ("medium", "xhigh"):
        errors.append("multilingual eval model profiles must be medium and xhigh")
    required_families = {str(item) for item in replay.get("required_model_families", [])}
    if not {"international-mainstream", "DeepSeek", "Qwen", "local-model"} <= required_families:
        errors.append("multilingual eval must name mainstream, DeepSeek, Qwen, and local-model coverage")
    if replay.get("status") not in ("not_run", "passed"):
        errors.append("multilingual eval replay status must be not_run or passed")
    if replay.get("status") == "not_run" and not str(replay.get("reason", "")).strip():
        errors.append("multilingual eval not_run status must include a reason")
    market_cases = spec.get("global_market_cases")
    if not isinstance(market_cases, list):
        errors.append("multilingual eval global_market_cases must be a list")
    else:
        by_id = {case.get("id"): case for case in market_cases if isinstance(case, dict)}
        for case_id, locale, market, platforms in EXPECTED_GLOBAL_MARKETS:
            case = by_id.get(case_id)
            if case is None:
                errors.append(f"multilingual eval is missing global market case {case_id}")
                continue
            if tuple(case.get(key) for key in ("locale", "target_market", "platforms")) != (locale, market, platforms):
                errors.append(f"multilingual eval global market case {case_id} has incorrect routing")
            if case.get("status") != "not_run":
                errors.append(f"multilingual eval global market case {case_id} must remain not_run")
            required_layers = set(case.get("required_query_layers", []))
            if not {"target-market-main-language", "English", "original-artist-title"} <= required_layers:
                errors.append(f"multilingual eval global market case {case_id} lacks query-language coverage")
    return errors


def validate_existing_eval_coverage() -> list[str]:
    """Ensure the existing eval files index every locale without replacing old cases."""
    errors: list[str] = []
    try:
        trigger_cases = json.loads(TRIGGER_EVAL_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"trigger evals cannot be read: {exc}"]
    localized_triggers = [
        case for case in trigger_cases
        if isinstance(case, dict)
        and case.get("case_type") == "baseline_direct"
        and "locale" in case
    ] if isinstance(trigger_cases, list) else []
    trigger_locales = [case.get("locale") for case in localized_triggers]
    if tuple(trigger_locales) != EXPECTED_LOCALES or len(set(trigger_locales)) != len(EXPECTED_LOCALES):
        errors.append("trigger evals must contain one baseline direct trigger per locale")

    try:
        legacy_cases = json.loads(LEGACY_TRIGGER_EVAL_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return errors + [f"legacy trigger evals cannot be read: {exc}"]
    if not isinstance(legacy_cases, list) or len(legacy_cases) < 61:
        errors.append("legacy trigger evals must retain the pre-semantic regression corpus")
    else:
        for index, case in enumerate(legacy_cases):
            if not isinstance(case, dict) or not isinstance(case.get("query"), str) or not isinstance(case.get("should_trigger"), bool):
                errors.append(f"legacy trigger eval case[{index}] must retain query and should_trigger fields")
                break

    try:
        intake_fixtures = json.loads(INTAKE_FIXTURE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return errors + [f"intake fixtures cannot be read: {exc}"]
    if not isinstance(intake_fixtures, dict) or tuple(
        intake_fixtures.get("locale_template_smoke", [])
    ) != EXPECTED_LOCALES:
        errors.append("intake fixtures must index all 26 locale templates")
    return errors


def validate_trigger_routing_cases() -> list[str]:
    """Keep the direct-versus-ambiguous trigger boundary explicit."""
    expected_routes = {
        "做个 playlist": "ambiguous_confirmation",
        "帮我做一张歌单": "ambiguous_confirmation",
        "/DJ": "ambiguous_confirmation",
        "DJ": "ambiguous_confirmation",
        "挖歌": "direct",
        "帮我排一个set 张三妹john summit风格的 edm house 综合版 8首歌": "direct",
    }
    try:
        cases = json.loads(TRIGGER_EVAL_PATH.read_text(encoding="utf-8"))
        legacy_cases = json.loads(LEGACY_TRIGGER_EVAL_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"trigger routing cases cannot be read: {exc}"]
    if not isinstance(cases, list):
        cases = []
    if isinstance(legacy_cases, list):
        cases = cases + legacy_cases
    indexed = {
        case.get("query"): case
        for case in cases
        if isinstance(case, dict) and "query" in case
    } if isinstance(cases, list) else {}
    errors: list[str] = []
    trigger_path = ROOT / "references" / "locales" / "stages" / "zh-Hans" / "trigger.json"
    try:
        trigger = json.loads(trigger_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"zh-Hans trigger resource cannot be read: {exc}"]
    direct_cues = trigger.get("direct", [])
    if not isinstance(direct_cues, list):
        return ["zh-Hans trigger resource direct cues must be a list"]
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for query, route in expected_routes.items():
        case = indexed.get(query)
        if case is None or case.get("expected_route") != route:
            errors.append(f"trigger routing case {query!r} must declare {route}")
        if route == "direct" and not any(
            isinstance(cue, str) and cue and cue in query for cue in direct_cues
        ):
            errors.append(
                f"direct trigger case {query!r} has no matching zh-Hans direct cue"
            )
        if query.startswith("帮我排一个set") and "排一个set" not in skill_text:
            errors.append(
                "SKILL.md frontmatter capsule is missing the reported zh-Hans trigger variant"
            )
    return errors


def main() -> int:
    trigger_contract, trigger_contract_failures = validate_trigger_signal_contract()
    manifest, failures = validate_manifest()
    failures.extend(trigger_contract_failures)
    failures.extend(validate_trigger_projections(trigger_contract, manifest))
    if MANIFEST_PATH.exists():
        entries = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")).get("locales", [])
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            locale = entry.get("id")
            filename = entry.get("file")
            if locale in EXPECTED_LOCALES and isinstance(filename, str):
                path = LOCALES_DIR / filename
                if path.exists():
                    try:
                        failures.extend(validate_pack(load_pack(path), locale))
                    except ValueError as exc:
                        failures.append(str(exc))
    failures.extend(validate_fixtures())
    failures.extend(validate_action_fixtures())
    failures.extend(validate_multilingual_eval_spec())
    failures.extend(validate_existing_eval_coverage())
    failures.extend(validate_trigger_routing_cases())
    failures.extend(validate_trigger_acceptance.validate_file())
    failures.extend(validate_language_routing.validate_contract())
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"PASS: {len(EXPECTED_LOCALES)} locale packs, report/action/status contracts, and fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
