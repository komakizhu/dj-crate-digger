#!/usr/bin/env python3
"""Generate the deterministic 100-case trigger acceptance matrix.

The old trigger fixture is copied to a separate regression file before the
canonical matrix is written.  The canonical matrix is intentionally authored
from the routing contract: its expected values are part of the test oracle,
while the validator independently runs the portable reference router.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "references" / "trigger-signals.json"
TRIGGER_EVAL_PATH = ROOT / "evals" / "trigger-evals.json"
LEGACY_PATH = ROOT / "evals" / "trigger-regression-legacy.json"

LOCALES = (
    "en", "zh-Hans", "zh-Hant", "es", "pt", "fr", "de", "ja", "ko", "ar",
    "ru", "tr", "hi", "id", "vi", "th", "it", "nl", "pl", "uk", "fa", "bn",
    "ur", "ms", "fil", "sw",
)

LANGUAGE_NAMES = {
    "en": "English",
    "zh-Hans": "简体中文",
    "zh-Hant": "繁體中文",
    "es": "Español",
    "pt": "Português",
    "fr": "Français",
    "de": "Deutsch",
    "ja": "日本語",
    "ko": "한국어",
    "ar": "العربية",
    "ru": "Русский",
    "tr": "Türkçe",
    "hi": "हिन्दी",
    "id": "Bahasa Indonesia",
    "vi": "Tiếng Việt",
    "th": "ไทย",
    "it": "Italiano",
    "nl": "Nederlands",
    "pl": "Polski",
    "uk": "Українська",
    "fa": "فارسی",
    "bn": "বাংলা",
    "ur": "اردو",
    "ms": "Bahasa Melayu",
    "fil": "Filipino",
    "sw": "Kiswahili",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def signals(
    *,
    language_locked: bool = True,
    clear_dj_context: bool = True,
    initial_message: bool = True,
    scene_or_purpose: bool = True,
    core_sound_or_reference: bool = True,
    count_or_duration: bool = True,
    explicit_output_mode: str | None = None,
    explicit_delegation: bool = False,
) -> dict[str, Any]:
    return {
        "language_locked": language_locked,
        "web_search": True,
        "open_page": True,
        "clear_dj_context": clear_dj_context,
        "initial_message": initial_message,
        "explicit_output_mode": explicit_output_mode,
        "intake_choice": None,
        "explicit_delegation": explicit_delegation,
        "scene_or_purpose": scene_or_purpose,
        "core_sound_or_reference": core_sound_or_reference,
        "count_or_duration": count_or_duration,
    }


def make_case(
    *,
    case_id: str,
    case_type: str,
    locale: str,
    text: str,
    style_family: str,
    signal_families: list[str],
    confidence: str,
    skill_route: str,
    intake_route: str,
    intake_signals: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": case_id,
        "case_type": case_type,
        "locale": locale,
        "language": LANGUAGE_NAMES[locale],
        "input": text,
        "query": text,
        "style_family": style_family,
        "signal_families": signal_families,
        "expected_confidence": confidence,
        "expected_host_invocation": "must_invoke" if skill_route != "non_trigger" else "must_not_invoke",
        "expected_skill_route": skill_route,
        "expected_route": skill_route,
        "expected_intake_route": intake_route,
        "intake_signals": intake_signals or signals(clear_dj_context=False),
        "should_trigger": skill_route == "direct",
    }


def main() -> int:
    contract = load_json(CONTRACT_PATH)
    overlays = contract.get("locale_overlays")
    if not isinstance(overlays, dict):
        raise ValueError("trigger contract is missing locale overlays")
    old_cases = load_json(LEGACY_PATH) if LEGACY_PATH.exists() else load_json(TRIGGER_EVAL_PATH)
    if not isinstance(old_cases, list):
        raise ValueError("existing trigger evals must be a list")
    old_by_locale = {
        case.get("locale"): case
        for case in old_cases
        if isinstance(case, dict) and case.get("locale") in LOCALES
    }
    missing = [locale for locale in LOCALES if locale not in old_by_locale]
    if missing:
        raise ValueError(f"existing localized trigger cases are missing: {missing}")

    # Preserve every pre-existing case as an explicit regression corpus.  Once
    # the archive exists, reuse it so regenerating the canonical matrix never
    # archives the generated matrix itself.
    if not LEGACY_PATH.exists():
        LEGACY_PATH.write_text(
            json.dumps(old_cases, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    cases: list[dict[str, Any]] = []
    for locale in LOCALES:
        direct = old_by_locale[locale]["query"]
        cases.append(make_case(
            case_id=f"baseline-direct-{locale}",
            case_type="baseline_direct",
            locale=locale,
            text=direct,
            style_family="uk_bass",
            signal_families=["dj_action", "dj_object", "dj_context", "genre", "set_detail"],
            confidence="very_high",
            skill_route="direct",
            intake_route="direct_ready",
            intake_signals=signals(),
        ))

    # Keep the exact generic boundary probes in the per-locale baseline set.
    exact_ambiguous = {"zh-Hans": "做个 playlist", "en": "DJ"}
    for locale in LOCALES:
        overlay = overlays[locale]
        generic = exact_ambiguous.get(locale, overlay["generic_music_term"][0])
        cases.append(make_case(
            case_id=f"baseline-ambiguous-{locale}",
            case_type="baseline_ambiguous",
            locale=locale,
            text=generic,
            style_family="none",
            signal_families=["dj_object"],
            confidence="medium" if generic == "DJ" else "low",
            skill_route="ambiguous_confirmation",
            intake_route="not_applicable",
        ))

    for locale in LOCALES:
        negative = overlays[locale]["negative_context"][0]
        cases.append(make_case(
            case_id=f"baseline-negative-{locale}",
            case_type="baseline_negative",
            locale=locale,
            text=negative,
            style_family="none",
            signal_families=["negative_context"],
            confidence="low",
            skill_route="non_trigger",
            intake_route="not_applicable",
        ))

    mode_cases = [
        ("zh-Hans", "综合版 House DJ set，给我排 8 首暖场歌", "composite"),
        ("zh-Hant", "綜合版 Techno DJ set，請排 8 首暖場歌", "composite"),
        ("en", "Rich Drum & Bass DJ set for a closing set", "four_views"),
        ("es", "modo rápido: prepara un set de Techno para un club", "fast"),
        ("ja", "完全版のJungle DJセットを作って", "four_views"),
        ("de", "Brief Techno Playlist für den Club", "composite"),
    ]
    for index, (locale, text, mode) in enumerate(mode_cases, start=1):
        cases.append(make_case(
            case_id=f"stress-mode-{index}",
            case_type="stress_mode",
            locale=locale,
            text=text,
            style_family="electronic_mix",
            signal_families=["mode", "dj_object", "genre", "dj_context"],
            confidence="very_high",
            skill_route="direct",
            intake_route="route_choice_pending",
            intake_signals=signals(
                scene_or_purpose=True,
                core_sound_or_reference=True,
                count_or_duration=False,
                explicit_output_mode=mode,
            ),
        ))

    genre_groups = [
        ("house,disco,techno", "House, Disco and Techno"),
        ("dubstep,bass,drum_and_bass", "Dubstep, Bass Music and Drum & Bass"),
        ("breakbeat,jungle,garage", "Breakbeat, Jungle and UK Garage"),
        ("trance,psytrance,progressive", "Trance, Psytrance and Progressive"),
        ("electro,future_bass,big_room", "Electro, Future Bass and Big Room"),
        ("hard_dance,hardcore,melodic_techno", "Hard Dance, Hardcore and Melodic Techno"),
    ]
    for index, (families, genres) in enumerate(genre_groups, start=1):
        cases.append(make_case(
            case_id=f"stress-genre-{index}",
            case_type="stress_genre",
            locale="en",
            text=f"Curate a DJ set with {genres} for a club dancefloor, 20 tracks.",
            style_family=families,
            signal_families=["dj_action", "dj_object", "dj_context", "genre", "set_detail"],
            confidence="very_high",
            skill_route="direct",
            intake_route="direct_ready",
            intake_signals=signals(),
        ))

    normalization_cases = [
        ("zh-Hans", "挖歌", "electronic_mix", "direct", "high", "round_1", signals(scene_or_purpose=False, core_sound_or_reference=False, count_or_duration=False)),
        ("en", "BUILD A DJ SET for a club: 12 DnB tracks!", "drum_and_bass", "direct", "very_high", "direct_ready", signals()),
        ("zh-Hans", "帮我排一个 set，House / Tech-House，8 首歌。", "house", "direct", "very_high", "direct_ready", signals()),
        ("zh-Hans", "帮我排一个set 张三妹john summit风格的 edm house 综合版 8首歌", "house", "direct", "very_high", "direct_ready", signals(explicit_output_mode="composite")),
    ]
    for index, (locale, text, style, route, confidence, intake, intake_signals) in enumerate(normalization_cases, start=1):
        cases.append(make_case(
            case_id=f"stress-normalization-{index}",
            case_type="stress_normalization",
            locale=locale,
            text=text,
            style_family=style,
            signal_families=["dj_action", "dj_object"] if route == "direct" else ["dj_object"],
            confidence=confidence,
            skill_route=route,
            intake_route=intake,
            intake_signals=intake_signals,
        ))

    mixed_cases = [
        ("zh-Hans", "帮我做一个 playlist，House House House warm-up，8 tracks", "house"),
        ("en", "Build 一套 DJ set for 周五 club，Deep House，10 tracks", "house"),
        ("en", "Curate a DJ set like John Summit，House / Tech House，8 tracks", "house"),
    ]
    for index, (locale, text, style) in enumerate(mixed_cases, start=1):
        cases.append(make_case(
            case_id=f"stress-mixed-language-{index}",
            case_type="stress_mixed_language",
            locale=locale,
            text=text,
            style_family=style,
            signal_families=["dj_action", "dj_object", "dj_context", "genre", "reference", "set_detail"],
            confidence="very_high",
            skill_route="direct",
            intake_route="direct_ready",
            intake_signals=signals(),
        ))

    negative_cases = [
        ("en", "Use FastAPI to build a House playlist recommendation API", "house", "very_high"),
        ("en", "What is the difference between DnB and Jungle?", "drum_and_bass,jungle", "low"),
        ("zh-Hans", "帮我下载 Techno 歌曲", "techno", "low"),
    ]
    for index, (locale, text, style, confidence) in enumerate(negative_cases, start=1):
        cases.append(make_case(
            case_id=f"stress-negative-override-{index}",
            case_type="stress_negative_override",
            locale=locale,
            text=text,
            style_family=style,
            signal_families=["negative_context", "genre", "dj_action", "dj_object"],
            confidence=confidence,
            skill_route="non_trigger",
            intake_route="not_applicable",
        ))

    if len(cases) != 100:
        raise AssertionError(f"generated {len(cases)} cases instead of 100")
    TRIGGER_EVAL_PATH.write_text(
        json.dumps(cases, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"PASS: wrote {len(cases)} canonical trigger cases and preserved {len(old_cases)} legacy cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
