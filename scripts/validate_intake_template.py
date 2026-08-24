#!/usr/bin/env python3
"""Validate rendered intake output against the canonical SKILL.md template."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = ROOT / "SKILL.md"
DEFAULT_FIXTURES = ROOT / "evals" / "intake-template-fixtures.json"
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")


def extract_template(skill_text: str, round_number: int) -> str:
    start = f"<!-- INTAKE_TEMPLATE_ROUND_{round_number}_ZH_CN_START -->"
    end = f"<!-- INTAKE_TEMPLATE_ROUND_{round_number}_ZH_CN_END -->"
    if skill_text.count(start) != 1 or skill_text.count(end) != 1:
        raise ValueError(f"round {round_number}: template markers must occur exactly once")

    return skill_text.split(start, 1)[1].split(end, 1)[0].strip()


def audit_shape(text: str, round_number: int) -> list[str]:
    expected_inline_count = {1: 20, 2: 30}[round_number]
    errors: list[str] = []
    inline_count = len(INLINE_CODE_RE.findall(text))
    if inline_count != expected_inline_count:
        errors.append(
            f"round {round_number}: expected {expected_inline_count} inline-code spans, "
            f"found {inline_count}"
        )
    if len(re.findall(r"^```markdown$", text, flags=re.MULTILINE)) != 1:
        errors.append(f"round {round_number}: expected exactly one markdown opening fence")
    if len(re.findall(r"^```$", text, flags=re.MULTILINE)) != 1:
        errors.append(f"round {round_number}: expected exactly one closing fence")
    if "INTAKE_TEMPLATE_" in text or "````" in text:
        errors.append(f"round {round_number}: authoring delimiters leaked into user output")
    if round_number == 1 and "填写规则为：" not in text:
        errors.append("round 1: missing exact literal '填写规则为：'")
    if round_number == 1:
        if text.count("输出版本：") != 2:
            errors.append("round 1: output version must appear in the prompt and fill-in block")
        if "「`极速版`：快速输出playlist，但是质量会下降」" not in text:
            errors.append("round 1: missing fast output-version definition")
        if "「`简要版`：只给一个综合的playlist」" not in text:
            errors.append("round 1: missing composite output-version definition")
        if "「`丰富版`：根据您选择的风格、场景、熟悉度与发现感分别提供建议，并最终输出成简要版」" not in text:
            errors.append("round 1: missing four-views output-version definition")
        if text.find("输出版本：") > text.find("其他限制："):
            errors.append("round 1: output version must precede other restrictions")
    else:
        if "输出版本" in text:
            errors.append("round 2: output version must be collected in round 1")
    return errors


def validate_output(actual: str, expected: str, round_number: int) -> list[str]:
    errors = audit_shape(actual, round_number)
    if actual.strip() != expected.strip():
        diff = "\n".join(
            difflib.unified_diff(
                expected.strip().splitlines(),
                actual.strip().splitlines(),
                fromfile="canonical",
                tofile="actual",
                lineterm="",
            )
        )
        errors.append(f"round {round_number}: output is not a literal template match\n{diff}")
    return errors


def run_self_test(skill_path: Path, fixture_path: Path) -> int:
    skill_text = skill_path.read_text(encoding="utf-8")
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for round_number in (1, 2):
        canonical = extract_template(skill_text, round_number)
        canonical_errors = validate_output(canonical, canonical, round_number)
        if canonical_errors:
            failures.extend(canonical_errors)

    for fixture in fixtures["negative_outputs"]:
        round_number = int(fixture["round"])
        canonical = extract_template(skill_text, round_number)
        if not validate_output(fixture["output"], canonical, round_number):
            failures.append(f"negative fixture unexpectedly passed: {fixture['name']}")

    if failures:
        print("\n\n".join(failures), file=sys.stderr)
        return 1
    print(
        f"PASS: 2 canonical templates accepted; "
        f"{len(fixtures['negative_outputs'])} regression outputs rejected"
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, default=DEFAULT_SKILL)
    parser.add_argument("--fixtures", type=Path, default=DEFAULT_FIXTURES)
    parser.add_argument("--round", type=int, choices=(1, 2))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path, help="UTF-8 model output to validate")
    group.add_argument("--emit-canonical", action="store_true")
    group.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if not args.self_test and args.round is None:
        parser.error("--round is required with --output or --emit-canonical")
    return args


def main() -> int:
    args = parse_args()
    if args.self_test:
        return run_self_test(args.skill, args.fixtures)

    skill_text = args.skill.read_text(encoding="utf-8")
    canonical = extract_template(skill_text, args.round)
    if args.emit_canonical:
        print(canonical)
        return 0

    actual = args.output.read_text(encoding="utf-8")
    errors = validate_output(actual, canonical, args.round)
    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: round {args.round} output exactly matches the canonical template")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
