#!/usr/bin/env python3
"""Run the 100-case matrix at a workspace, package, or installed-copy seam."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from trigger_router import classify, load_contract
from validate_intake_routing import route as intake_route


SCRIPT_ROOT = Path(__file__).resolve().parents[1]


def run(root: Path) -> dict[str, Any]:
    fixture_path = root / "evals" / "trigger-evals.json"
    contract_path = root / "references" / "trigger-signals.json"
    cases = json.loads(fixture_path.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise ValueError("trigger acceptance fixture must be a list")
    contract = load_contract(contract_path)
    results: list[dict[str, Any]] = []
    locale_coverage: dict[str, dict[str, int]] = {}
    genre_coverage: dict[str, int] = {family: 0 for family in contract.get("genre_families", {})}
    for case in cases:
        reference = classify(case["input"], case["locale"], contract=contract)
        if reference["skill_route"] == "direct":
            actual_intake = intake_route(case["intake_signals"])["route"]
        else:
            actual_intake = "not_applicable"
        static_pass = (
            reference["host_invocation"] == case["expected_host_invocation"]
            and reference["skill_route"] == case["expected_skill_route"]
            and reference["confidence"] == case["expected_confidence"]
            and actual_intake == case["expected_intake_route"]
        )
        locale_stats = locale_coverage.setdefault(case["locale"], {"total": 0, "passed": 0})
        locale_stats["total"] += 1
        if static_pass:
            locale_stats["passed"] += 1
        for family in reference["matches"].get("genre", {}):
            if family in genre_coverage:
                genre_coverage[family] += 1
        results.append({
            "id": case["id"],
            "case_type": case["case_type"],
            "locale": case["locale"],
            "language": case["language"],
            "input": case["input"],
            "query": case["query"],
            "style_family": case["style_family"],
            "signal_families": case["signal_families"],
            "expected_confidence": case["expected_confidence"],
            "expected_host_invocation": case["expected_host_invocation"],
            "expected_skill_route": case["expected_skill_route"],
            "expected_intake_route": case["expected_intake_route"],
            # The portable reference router can predict the host decision, but
            # this run has no external host load trace. Keep the actual field
            # honest and expose the prediction as evidence instead.
            "actual_host_invocation": "not_observed",
            "actual_skill_route": reference["skill_route"],
            "actual_intake_route": actual_intake,
            "actual_confidence": reference["confidence"],
            "evidence": {
                "execution_layer": "portable_reference_router",
                "host_invocation_observed": False,
                "reference_host_invocation": reference["host_invocation"],
                "matched_signals": reference["matches"],
                "score": reference["score"],
                "contributions": reference["contributions"],
            },
            "pass": static_pass,
        })
    static_pass = len(results) == 100 and all(result["pass"] for result in results)
    return {
        "schema": "dj-crate-digger-trigger-acceptance-results",
        "schema_version": 1,
        "source_root": str(root),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "execution_layer": "portable_reference_router",
        "host_e2e_status": "not_run",
        "host_invocation_observed": False,
        "static_status": "passed" if static_pass else "failed",
        "overall_status": "static_pass_host_unverified" if static_pass else "failed",
        "case_count": len(results),
        "passed_case_count": sum(1 for result in results if result["pass"]),
        "failed_case_count": sum(1 for result in results if not result["pass"]),
        "locale_coverage": locale_coverage,
        "genre_family_coverage": genre_coverage,
        "limitation": "No real host load trace is exposed in this execution environment; static reference results do not satisfy host end-to-end acceptance.",
        "cases": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=SCRIPT_ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    try:
        report = run(root)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(
        f"PASS: static trigger acceptance {report['passed_case_count']}/{report['case_count']}; "
        f"host_e2e_status={report['host_e2e_status']}"
    )
    return 0 if report["static_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
