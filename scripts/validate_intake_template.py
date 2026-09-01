#!/usr/bin/env python3
"""Validate rendered intake output against a fixed locale-pack template."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = ROOT / "SKILL.md"
DEFAULT_LOCALE_DIR = ROOT / "references" / "locales"
DEFAULT_FIXTURES = ROOT / "evals" / "intake-template-fixtures.json"
DEFAULT_LOCALE = "zh-Hans"
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)


def load_locale_pack(locale_dir: Path, locale: str) -> dict[str, Any]:
    path = locale_dir / f"{locale}.md"
    text = path.read_text(encoding="utf-8")
    matches = JSON_FENCE_RE.findall(text)
    if len(matches) != 1:
        raise ValueError(f"{path}: expected exactly one JSON code block")
    value = json.loads(matches[0])
    if not isinstance(value, dict) or value.get("locale") != locale:
        raise ValueError(f"{path}: locale metadata does not match {locale!r}")
    return value


def extract_legacy_template(skill_text: str, round_number: int) -> str:
    """Read the pre-locale marker format for callers with an older SKILL.md."""
    start = f"<!-- INTAKE_TEMPLATE_ROUND_{round_number}_ZH_CN_START -->"
    end = f"<!-- INTAKE_TEMPLATE_ROUND_{round_number}_ZH_CN_END -->"
    if skill_text.count(start) != 1 or skill_text.count(end) != 1:
        raise ValueError(f"round {round_number}: legacy template markers must occur exactly once")
    return skill_text.split(start, 1)[1].split(end, 1)[0].strip()


def extract_template(source: str | Path, round_number: int, locale: str = DEFAULT_LOCALE) -> str:
    """Extract a prompt from a locale pack, with legacy SKILL compatibility."""
    text = source.read_text(encoding="utf-8") if isinstance(source, Path) else source
    if "INTAKE_TEMPLATE_ROUND_" in text:
        return extract_legacy_template(text, round_number)
    matches = JSON_FENCE_RE.findall(text)
    if len(matches) != 1:
        raise ValueError("locale source must contain exactly one JSON code block")
    pack = json.loads(matches[0])
    return str(pack["intake"][f"round_{round_number}"]["prompt"]).strip()


def locale_prompt(locale_dir: Path, locale: str, round_number: int) -> str:
    pack = load_locale_pack(locale_dir, locale)
    return str(pack["intake"][f"round_{round_number}"]["prompt"]).strip()


def audit_shape(text: str, round_number: int, locale: str = DEFAULT_LOCALE) -> list[str]:
    errors: list[str] = []
    if locale == DEFAULT_LOCALE:
        expected_inline_count = {1: 20, 2: 30}[round_number]
        inline_count = len(INLINE_CODE_RE.findall(text))
        if inline_count != expected_inline_count:
            errors.append(
                f"{locale} round {round_number}: expected {expected_inline_count} inline-code spans, found {inline_count}"
            )
    if len(re.findall(r"^```markdown$", text, flags=re.MULTILINE)) != 1:
        errors.append(f"{locale} round {round_number}: expected exactly one markdown opening fence")
    if len(re.findall(r"^```$", text, flags=re.MULTILINE)) != 1:
        errors.append(f"{locale} round {round_number}: expected exactly one closing fence")
    if "INTAKE_TEMPLATE_" in text or "````" in text:
        errors.append(f"{locale} round {round_number}: authoring delimiters leaked into user output")
    if round_number == 1 and locale == DEFAULT_LOCALE:
        if text.count("输出版本：") != 2:
            errors.append("zh-Hans round 1: output version must appear in prompt and fill-in block")
        if "填写规则为：" not in text:
            errors.append("zh-Hans round 1: missing exact literal '填写规则为：'")
        if "「`极速版`：快速输出playlist，但是质量会下降」" not in text:
            errors.append("zh-Hans round 1: missing fast output-version definition")
        if "「`综合版`：只给一个综合的playlist」" not in text:
            errors.append("zh-Hans round 1: missing composite output-version definition")
        if "「`完整版`：根据您选择的风格、场景、熟悉度与发现感分别提供建议，并最终输出成综合版」" not in text:
            errors.append("zh-Hans round 1: missing full output-version definition")
        if "简要版" in text or "丰富版" in text:
            errors.append("zh-Hans round 1: legacy output labels must not appear in the new prompt")
    elif round_number == 2 and locale == DEFAULT_LOCALE and "输出版本" in text:
        errors.append("zh-Hans round 2: output version must be collected in round 1")
    return errors


def validate_output(actual: str, expected: str, round_number: int, locale: str = DEFAULT_LOCALE) -> list[str]:
    errors = audit_shape(actual, round_number, locale)
    if actual.strip() != expected.strip():
        diff = "\n".join(
            difflib.unified_diff(
                expected.strip().splitlines(),
                actual.strip().splitlines(),
                fromfile=f"{locale}-canonical",
                tofile="actual",
                lineterm="",
            )
        )
        errors.append(f"{locale} round {round_number}: output is not a literal template match\n{diff}")
    return errors


def manifest_locales(locale_dir: Path) -> list[str]:
    manifest = json.loads((locale_dir / "manifest.json").read_text(encoding="utf-8"))
    return [str(item["id"]) for item in manifest["locales"]]


def run_self_test(locale_dir: Path, fixture_path: Path) -> int:
    failures: list[str] = []
    locales = manifest_locales(locale_dir)
    for locale in locales:
        for round_number in (1, 2):
            canonical = locale_prompt(locale_dir, locale, round_number)
            failures.extend(validate_output(canonical, canonical, round_number, locale))

    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    for fixture in fixtures["negative_outputs"]:
        round_number = int(fixture["round"])
        canonical = locale_prompt(locale_dir, DEFAULT_LOCALE, round_number)
        if not validate_output(fixture["output"], canonical, round_number, DEFAULT_LOCALE):
            failures.append(f"negative fixture unexpectedly passed: {fixture['name']}")

    if failures:
        print("\n\n".join(failures), file=sys.stderr)
        return 1
    print(f"PASS: {len(locales)} locale templates accepted; {len(fixtures['negative_outputs'])} regression outputs rejected")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, default=DEFAULT_SKILL, help="legacy SKILL.md source, if supplied")
    parser.add_argument("--locale-dir", type=Path, default=DEFAULT_LOCALE_DIR)
    parser.add_argument("--locale", default=DEFAULT_LOCALE)
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
        return run_self_test(args.locale_dir, args.fixtures)
    source = args.skill if args.skill.exists() and "INTAKE_TEMPLATE_ROUND_" in args.skill.read_text(encoding="utf-8") else args.locale_dir / f"{args.locale}.md"
    canonical = extract_template(source, args.round, args.locale)
    if args.emit_canonical:
        print(canonical)
        return 0
    actual = args.output.read_text(encoding="utf-8")
    errors = validate_output(actual, canonical, args.round, args.locale)
    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {args.locale} round {args.round} output exactly matches the canonical template")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
