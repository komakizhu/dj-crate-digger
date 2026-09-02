#!/usr/bin/env python3
"""Compare package-owned files without deleting target-only local files."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

from build_skill_package import EXCLUDED_DIRS, EXCLUDED_SUFFIXES, package_files


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def target_files(root: Path) -> set[Path]:
    result: set[Path] = set()
    if not root.exists():
        return result
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_file() and path.suffix not in EXCLUDED_SUFFIXES and path.name != ".DS_Store":
            result.add(relative)
    return result


def parity(source: Path, target: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []
    source_set = set(package_files(source))
    target_set = target_files(target)
    for relative in sorted(source_set - target_set):
        errors.append(f"missing target file: {relative}")
    for relative in sorted(target_set - source_set):
        notes.append(f"preserved target-only file: {relative}")
    for relative in sorted(source_set & target_set):
        if digest(source / relative) != digest(target / relative):
            errors.append(f"content mismatch: {relative}")
    return errors, notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    if not source.is_dir() or not target.is_dir():
        print(f"FAIL: source and target must be directories: {source}, {target}", file=sys.stderr)
        return 1
    errors, notes = parity(source, target)
    for note in notes:
        print(f"NOTE: {note}")
    if errors:
        print("FAIL: package parity", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: package-owned files are byte-identical ({len(package_files(source))} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
