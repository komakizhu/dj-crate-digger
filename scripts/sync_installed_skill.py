#!/usr/bin/env python3
"""Safely sync package-owned files to an explicitly named installed copy."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from build_skill_package import EXCLUDED_DIRS, EXCLUDED_SUFFIXES, package_files
from validate_package_parity import parity


PRESERVED_PREFIXES = ("test-artifacts/",)


def all_files(root: Path) -> set[Path]:
    if not root.exists():
        return set()
    result: set[Path] = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_file() and path.suffix not in EXCLUDED_SUFFIXES and path.name != ".DS_Store":
            result.add(relative)
    return result


def sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def unexpected_target_files(source: Path, target: Path) -> list[Path]:
    expected = set(package_files(source))
    unexpected: set[Path] = set()
    for path in target.rglob("*"):
        relative = path.relative_to(target)
        relative_text = relative.as_posix()
        if any(relative_text.startswith(prefix) for prefix in PRESERVED_PREFIXES):
            continue
        if ".git" in relative.parts or "__pycache__" in relative.parts:
            unexpected.add(next((Path(part) for part in relative.parts if part in {".git", "__pycache__"}), relative))
            continue
        if path.is_file() and path.suffix not in EXCLUDED_SUFFIXES and path.name != ".DS_Store" and relative not in expected:
            unexpected.add(relative)
    return sorted(unexpected)


def snapshot(target: Path, backup_root: Path) -> dict[str, object]:
    backup_root.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, str]] = []
    for relative in sorted(all_files(target)):
        source_path = target / relative
        backup_path = backup_root / relative
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, backup_path)
        records.append({"path": relative.as_posix(), "sha256": sha256(source_path)})
    manifest = {
        "schema": "dj-crate-digger-installed-snapshot",
        "target": str(target),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "files": records,
    }
    (backup_root / "snapshot.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def sync(source: Path, target: Path, backup_root: Path) -> tuple[int, int, dict[str, object]]:
    target.mkdir(parents=True, exist_ok=True)
    manifest = snapshot(target, backup_root)
    extra = unexpected_target_files(source, target)
    if extra:
        raise ValueError(
            "unexpected target files found; no package files were changed; "
            f"snapshot is at {backup_root}: "
            + ", ".join(path.as_posix() for path in extra)
        )
    copied = 0
    for relative in package_files(source):
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, destination)
        copied += 1
    return copied, len(manifest["files"]), manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--backup-root", type=Path)
    parser.add_argument("--apply", action="store_true", help="copy package-owned files")
    args = parser.parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    if not source.is_dir():
        print(f"FAIL: source is not a directory: {source}", file=sys.stderr)
        return 1
    if target == source:
        print("FAIL: source and target must be different directories", file=sys.stderr)
        return 1

    if not args.apply:
        errors, notes = parity(source, target)
        for note in notes:
            print(f"NOTE: {note}")
        if errors:
            print("FAIL: installed copy is not in parity (dry run)", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print("PASS: installed copy is already in parity (dry run)")
        return 0

    backup_root = args.backup_root or (
        source / "test-artifacts" / "installed-backups" /
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    )
    try:
        copied, snapshotted, manifest = sync(source, target, backup_root.resolve())
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: synced {copied} package files to {target}")
    print(f"NOTE: snapshotted {snapshotted} existing target files at {backup_root.resolve()}")
    print(f"NOTE: target-only preserved prefixes: {', '.join(PRESERVED_PREFIXES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
