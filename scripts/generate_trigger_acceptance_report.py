#!/usr/bin/env python3
"""Render a bilingual Markdown report from static trigger result runs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_package_parity import parity


ROOT = Path(__file__).resolve().parents[1]
LOCALE_ORDER = (
    "en", "zh-Hans", "zh-Hant", "es", "pt", "fr", "de", "ja", "ko", "ar",
    "ru", "tr", "hi", "id", "vi", "th", "it", "nl", "pl", "uk", "fa", "bn",
    "ur", "ms", "fil", "sw",
)


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"result report must be an object: {path}")
    return value


def evidence_text(evidence: dict[str, Any]) -> str:
    compact = json.dumps(
        {
            "signals": evidence.get("matched_signals", {}),
            "score": evidence.get("score"),
            "contributions": evidence.get("contributions", {}),
            "reference_host": evidence.get("reference_host_invocation"),
            "host_observed": evidence.get("host_invocation_observed"),
            "layer": evidence.get("execution_layer"),
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return compact.replace("|", "\\|").replace("\n", " ")


def cell_text(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def render(result: dict[str, Any], package_parity: str, installed_parity: str) -> str:
    cases = result.get("cases", [])
    static_status = result.get("static_status", "unknown")
    host_status = result.get("host_e2e_status", "unknown")
    overall = result.get("overall_status", "unknown")
    lines = [
        "# 触发验收报告 / Trigger Acceptance Report",
        "",
        f"- 静态状态 / Static status: **{static_status}** ({result.get('passed_case_count', 0)}/{result.get('case_count', 0)})",
        f"- 宿主端到端 / Host end-to-end: **{host_status}**",
        f"- 总体状态 / Overall status: **{overall}**",
        "- 口径 / Rule: static reference success is not host end-to-end success; `not_run` is never promoted to `passed`.",
        "",
        "## 字段对照 / Field mapping",
        "",
        "| 中文 | English |",
        "|---|---|",
        "| 宿主是否调用 | Host invocation |",
        "| Skill 内部路由 | Skill route |",
        "| intake 路由 | Intake route |",
        "| 预期置信度 | Expected confidence |",
        "| 实际置信度 | Actual confidence |",
        "| 证据 | Evidence |",
        "| 通过/失败 | Pass/Fail |",
        "",
        "## 产物 parity / Artifact parity",
        "",
        "| Comparison | Result |",
        "|---|---|",
        f"| Workspace → clean package | {package_parity} |",
        f"| Workspace → installed copy | {installed_parity} |",
        "| Package contents | excludes `.git`, caches, temporary replay results, and `test-artifacts` |",
        "",
        "## 26 语言覆盖 / 26-locale coverage",
        "",
        "| Locale | Total | Passed |",
        "|---|---:|---:|",
    ]
    coverage = result.get("locale_coverage", {})
    for locale in LOCALE_ORDER:
        stats = coverage.get(locale, {})
        lines.append(f"| {locale} | {stats.get('total', 0)} | {stats.get('passed', 0)} |")
    lines.extend([
        "",
        "## 电子乐风格族覆盖 / Electronic genre-family coverage",
        "",
        "| Family | Matched case count |",
        "|---|---:|",
    ])
    for family, count in result.get("genre_family_coverage", {}).items():
        lines.append(f"| {family} | {count} |")
    lines.extend([
        "",
        "## 100 条逐条结果 / 100 row-level results",
        "",
        "| # | ID | Locale | Input / 原句 | Expected host | Actual host | Expected route | Actual route | Expected confidence | Actual confidence | Intake | Pass | Evidence |",
        "|---:|---|---|---|---|---|---|---|---|---|---|---|---|",
    ])
    for index, case in enumerate(cases, start=1):
        lines.append(
            "| {index} | {id} | {locale} | {input} | {expected_host} | {actual_host} | {expected_route} | {actual_route} | {expected_confidence} | {actual_confidence} | {intake} | {passed} | {evidence} |".format(
                index=index,
                id=case.get("id", ""),
                locale=case.get("locale", ""),
                input=cell_text(case.get("input", "")),
                expected_host=case.get("expected_host_invocation", ""),
                expected_route=case.get("expected_skill_route", ""),
                actual_route=case.get("actual_skill_route", ""),
                expected_confidence=case.get("expected_confidence", ""),
                actual_confidence=case.get("actual_confidence", ""),
                intake=case.get("actual_intake_route", ""),
                actual_host=case.get("actual_host_invocation", ""),
                passed="PASS" if case.get("pass") else "FAIL",
                evidence=evidence_text(case.get("evidence", {})),
            )
        )
    lines.extend([
        "",
        "## 限制 / Limitations",
        "",
        str(result.get("limitation", "")),
        "",
        "The existing 312-run multilingual cold-start replay remains an independent contract. Its declared status is not changed by this report.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-result", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--installed", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = load(args.workspace_result.resolve())
        package_errors, _ = parity(args.source.resolve(), args.package.resolve())
        installed_errors, _ = parity(args.source.resolve(), args.installed.resolve())
        package_status = "PASS" if not package_errors else "FAIL: " + "; ".join(package_errors[:3])
        installed_status = "PASS" if not installed_errors else "FAIL: " + "; ".join(installed_errors[:3])
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render(result, package_status, installed_status), encoding="utf-8")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: wrote bilingual 100-row acceptance report to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
