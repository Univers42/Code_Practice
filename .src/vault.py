#!/usr/bin/env python3
"""
Dev tool: lock/unlock statements, solutions and testers at rest, for every
rank (02, 03, 04).

Nothing under .src/.statements/rank*, .src/rank*/solutions or .src/rank*/testers
should ever sit in plain text in the tracked tree — not even for editing.
`unlock` writes to .vault_scratch/ (gitignored, outside the tracked trees),
never back over the encrypted original.

Usage:
  vault.py lock <file>                 encrypt <file> -> <file>.enc, remove the plaintext
  vault.py unlock <file>.enc [-o OUT]  decrypt to .vault_scratch/... (or -o OUT)
  vault.py lock-all                    encrypt every currently-plaintext file in scope
  vault.py verify-all                  decrypt every .enc in memory and check it; writes nothing
"""
import argparse
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
REPO_ROOT = SRC.parent
sys.path.insert(0, str(SRC / "shell" / "4_grading"))
from c_vault import DEFAULT_KEY_PATH, VaultError, decrypt_bytes, decrypt_file, encrypt_file  # noqa: E402

KEY_PATH = DEFAULT_KEY_PATH
SCRATCH = REPO_ROOT / ".vault_scratch"

# (directory, extensions) in scope for lock-all / verify-all, across every rank
TARGETS = []
for _rank in (2, 3, 4, 5):
    _rank_dir = SRC / f"rank{_rank:02d}"
    _sol_exts = {".c", ".h"} if _rank == 2 else {".py"}
    TARGETS.append((_rank_dir / "solutions", _sol_exts))
    TARGETS.append((_rank_dir / "testers", {".py"}))
    TARGETS.append((SRC / ".statements" / f"rank{_rank:02d}", {".txt"}))


def iter_plaintext_targets():
    for base, exts in TARGETS:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.suffix in exts:
                yield path


def iter_encrypted_targets():
    for base, _ in TARGETS:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.enc")):
            yield path


def cmd_lock(args) -> None:
    src = Path(args.file).resolve()
    dest = src.with_name(src.name + ".enc")
    encrypt_file(src, dest, KEY_PATH)
    src.unlink()
    print(f"locked: {src} -> {dest}")


def cmd_unlock(args) -> None:
    src = Path(args.file).resolve()
    if args.out:
        dest = Path(args.out)
    else:
        rel = src.relative_to(REPO_ROOT)
        rel_plain = rel.with_name(rel.name.removesuffix(".enc"))
        dest = SCRATCH / rel_plain
    dest.parent.mkdir(parents=True, exist_ok=True)
    decrypt_file(src, dest, KEY_PATH)
    print(f"unlocked (scratch, not tracked): {dest}")


def cmd_lock_all(args) -> None:
    n = 0
    for path in iter_plaintext_targets():
        dest = path.with_name(path.name + ".enc")
        encrypt_file(path, dest, KEY_PATH)
        path.unlink()
        n += 1
    print(f"locked {n} files")


def cmd_verify_all(args) -> None:
    n = 0
    bad = []
    for path in iter_encrypted_targets():
        try:
            decrypt_bytes(path.read_bytes(), KEY_PATH)
            n += 1
        except VaultError as error:
            bad.append((path, error))
    print(f"verified {n} files")
    for path, error in bad:
        print(f"  BAD: {path}: {error}")
    if bad:
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_lock = sub.add_parser("lock")
    p_lock.add_argument("file")
    p_lock.set_defaults(func=cmd_lock)

    p_unlock = sub.add_parser("unlock")
    p_unlock.add_argument("file")
    p_unlock.add_argument("-o", "--out")
    p_unlock.set_defaults(func=cmd_unlock)

    p_lock_all = sub.add_parser("lock-all")
    p_lock_all.set_defaults(func=cmd_lock_all)

    p_verify_all = sub.add_parser("verify-all")
    p_verify_all.set_defaults(func=cmd_verify_all)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
