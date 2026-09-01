#!/usr/bin/env python3
"""Validate the structured adaptive-intake routing contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "evals" / "intake-routing-fixtures.json"
VALID_MODES = {"fast", "composite", "four_views"}
VALID_INTAKE_CHOICES = {"direct", "questionnaire"}
PARTIAL_BRIEF_SIGNALS = (
    "scene_or_purpose",
    "core_sound_or_reference",
    "count_or_duration",
)


def route(signals: dict[str, Any]) -> dict[str, str | None]:
    if not signals.get("language_locked"):
        return {"route": "language_confirmation", "output_mode": None}
    if not signals.get("web_search") or not signals.get("open_page"):
        return {"route": "capability_error", "output_mode": None}
    if not signals.get("clear_dj_context"):
        return {"route": "not_triggered", "output_mode": None}

    explicit_mode = signals.get("explicit_output_mode")
    if explicit_mode is not None and explicit_mode not in VALID_MODES:
        raise ValueError(f"unsupported explicit_output_mode: {explicit_mode!r}")
    default_mode = explicit_mode or "composite"

    intake_choice = signals.get("intake_choice")
    if intake_choice is not None and intake_choice not in VALID_INTAKE_CHOICES:
        raise ValueError(f"unsupported intake_choice: {intake_choice!r}")
    if intake_choice == "direct":
        return {"route": "direct_ready", "output_mode": default_mode}
    if intake_choice == "questionnaire":
        return {"route": "round_1", "output_mode": default_mode}

    minimum_brief = all(
        signals.get(field)
        for field in ("scene_or_purpose", "core_sound_or_reference", "count_or_duration")
    )
    if bool(signals.get("explicit_delegation")) or (
        bool(signals.get("initial_message")) and minimum_brief
    ):
        return {"route": "direct_ready", "output_mode": default_mode}

    partial_signal_count = sum(
        bool(signals.get(field)) for field in PARTIAL_BRIEF_SIGNALS
    )
    if bool(signals.get("initial_message")) and partial_signal_count >= 2:
        return {"route": "route_choice_pending", "output_mode": default_mode}
    return {"route": "round_1", "output_mode": default_mode}


def main() -> int:
    try:
        payload = json.loads(FIXTURES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load intake routing fixtures: {exc}", file=sys.stderr)
        return 1

    failures: list[str] = []
    cases = payload.get("cases") if isinstance(payload, dict) else None
    if not isinstance(cases, list) or not cases:
        failures.append("fixtures must contain a non-empty cases list")
    else:
        seen: set[str] = set()
        for case in cases:
            case_id = str(case.get("id", "<missing>"))
            if case_id in seen:
                failures.append(f"duplicate case id: {case_id}")
                continue
            seen.add(case_id)
            try:
                actual = route(case["signals"])
                expected = case["expected"]
            except (KeyError, TypeError, ValueError) as exc:
                failures.append(f"{case_id}: invalid fixture: {exc}")
                continue
            if actual != expected:
                failures.append(f"{case_id}: expected {expected!r}, got {actual!r}")

    if failures:
        print("FAIL: adaptive intake routing", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"PASS: {len(cases)} adaptive intake routing cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
