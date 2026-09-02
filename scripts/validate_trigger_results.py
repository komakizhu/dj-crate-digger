#!/usr/bin/env python3
"""Validate the shape and honesty of a generated trigger result report."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_RESULT_KEYS = {
    "id",
    "locale",
    "language",
    "input",
    "style_family",
    "expected_confidence",
    "expected_host_invocation",
    "expected_skill_route",
    "expected_intake_route",
    "actual_host_invocation",
    "actual_skill_route",
    "actual_intake_route",
    "actual_confidence",
    "evidence",
    "pass",
}
VALID_ACTUAL_HOST_INVOCATIONS = {"must_invoke", "must_not_invoke", "not_observed"}
VALID_HOST_STATUSES = {"not_run", "passed", "failed", "not_observed"}


def validate(path: Path) -> list[str]:
    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load result report: {exc}"]
    if not isinstance(report, dict):
        return ["result report must contain an object"]
    errors: list[str] = []
    if report.get("schema") != "dj-crate-digger-trigger-acceptance-results":
        errors.append("unexpected result report schema")
    cases = report.get("cases")
    if not isinstance(cases, list) or len(cases) != 100:
        errors.append("result report must contain exactly 100 cases")
        cases = cases if isinstance(cases, list) else []
    ids: set[str] = set()
    host_status = report.get("host_e2e_status")
    if host_status not in VALID_HOST_STATUSES:
        errors.append("host_e2e_status must be an explicit known status")
    if host_status == "not_run" and report.get("host_invocation_observed") is not False:
        errors.append("host_e2e_status=not_run requires host_invocation_observed=false")
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case[{index}] must be an object")
            continue
        missing = REQUIRED_RESULT_KEYS - set(case)
        if missing:
            errors.append(f"case[{index}] missing fields: {sorted(missing)}")
        case_id = case.get("id")
        if case_id in ids:
            errors.append(f"duplicate result id: {case_id}")
        ids.add(case_id)
        evidence = case.get("evidence")
        if not isinstance(evidence, dict) or not evidence:
            errors.append(f"{case_id}: evidence must be a non-empty object")
        if not isinstance(case.get("pass"), bool):
            errors.append(f"{case_id}: pass must be boolean")
        if case.get("actual_host_invocation") not in VALID_ACTUAL_HOST_INVOCATIONS:
            errors.append(f"{case_id}: actual_host_invocation must be an observed value or not_observed")
        if isinstance(evidence, dict):
            if case.get("actual_host_invocation") == "not_observed" and evidence.get("host_invocation_observed") is not False:
                errors.append(f"{case_id}: not_observed host invocation requires host_invocation_observed=false")
            reference_host = evidence.get("reference_host_invocation")
            if reference_host not in {"must_invoke", "must_not_invoke"}:
                errors.append(f"{case_id}: evidence must retain the reference host prediction")
    if report.get("host_e2e_status") == "not_run" and report.get("overall_status") == "passed":
        errors.append("host_e2e_status=not_run cannot have overall_status=passed")
    if report.get("case_count") != len(cases):
        errors.append("case_count does not match result rows")
    if report.get("passed_case_count") != sum(1 for case in cases if isinstance(case, dict) and case.get("pass") is True):
        errors.append("passed_case_count does not match result rows")
    locale_coverage = report.get("locale_coverage")
    if not isinstance(locale_coverage, dict) or len(locale_coverage) != 26:
        errors.append("locale_coverage must contain all 26 locales")
    elif any(
        not isinstance(value, dict)
        or not isinstance(value.get("total"), int)
        or value.get("total", 0) < 3
        or not isinstance(value.get("passed"), int)
        or value.get("passed", -1) < 0
        or value.get("passed", 0) > value.get("total", 0)
        for value in locale_coverage.values()
    ):
        errors.append("locale_coverage entries must report at least three rows and valid pass counts")
    if not isinstance(report.get("genre_family_coverage"), dict) or len(report["genre_family_coverage"]) < 18:
        errors.append("genre_family_coverage must include the 18 central genre families")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    errors = validate(args.path.resolve())
    if errors:
        print("FAIL: trigger result report", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: trigger result report contains 100 complete, honest rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
