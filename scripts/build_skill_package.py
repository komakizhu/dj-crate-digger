#!/usr/bin/env python3
"""Build a clean, host-neutral dj-crate-digger package from this workspace."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "test-artifacts", "__pycache__"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def package_files(root: Path) -> list[Path]:
    """Return package-relative files, excluding repository/build artefacts."""
    files: list[Path] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_file() and path.suffix not in EXCLUDED_SUFFIXES and path.name != ".DS_Store":
            files.append(relative)
    return sorted(files)


def safe_replace_target(source: Path, output: Path) -> bool:
    artifacts = source / "test-artifacts"
    try:
        output.relative_to(artifacts)
    except ValueError:
        return False
    return output != source and output != artifacts


def build(source: Path, output: Path, replace: bool) -> list[Path]:
    source = source.resolve()
    output = output.resolve()
    if not source.is_dir():
        raise ValueError(f"source is not a directory: {source}")
    if output.exists():
        if not replace:
            raise ValueError(f"output already exists; pass --replace for a generated test-artifact: {output}")
        if not safe_replace_target(source, output):
            raise ValueError("--replace is restricted to a child of source/test-artifacts")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    copied: list[Path] = []
    for relative in package_files(source):
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, destination)
        copied.append(relative)
    return copied


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()
    try:
        copied = build(args.source, args.output, args.replace)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: built clean package with {len(copied)} files at {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
