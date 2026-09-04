"""Encryption at rest for rank02 subjects/solutions/testers.

Not a defense against a determined attacker with local admin rights — the
key lives in the same repo. The point is that nothing in .src/.subjects/rank02,
.src/rank02/solutions or .src/rank02/testers sits on disk in plain text:
each piece is decrypted only at the moment it's actually needed (a subject
when it's handed to the student, a reference/tester when a grading attempt
compiles it into its own ephemeral sandbox), and never written back out in
the clear anywhere permanent.

AES-256-CBC via the system `openssl` binary — no new Python dependency,
consistent with how the rest of the grading pipeline already shells out to
cc/nm rather than pulling in libraries. CBC alone doesn't authenticate, so
a corrupted ciphertext can decrypt to silent garbage instead of erroring
(confirmed experimentally); a SHA-256 of the plaintext travels inside the
encrypted payload so any corruption is caught explicitly instead of
producing a confusing downstream compiler error.
"""
import hashlib
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_KEY_PATH = REPO_ROOT / ".src" / ".vault_key"

OPENSSL_ARGS = ["-aes-256-cbc", "-pbkdf2", "-iter", "100000", "-md", "sha256", "-salt"]
RUN_TIMEOUT = 15.0


class VaultError(RuntimeError):
    pass


def _run_openssl(args: list[str], data: bytes) -> bytes:
    try:
        proc = subprocess.run(
            ["openssl", "enc", *args],
            input=data,
            capture_output=True,
            timeout=RUN_TIMEOUT,
        )
    except (subprocess.TimeoutExpired, OSError) as error:
        raise VaultError(f"openssl invocation failed: {error}") from error
    if proc.returncode != 0:
        raise VaultError(proc.stderr.decode(errors="replace").strip())
    return proc.stdout


def encrypt_bytes(plaintext: bytes, key_path: Path = DEFAULT_KEY_PATH) -> bytes:
    digest = hashlib.sha256(plaintext).hexdigest().encode()
    payload = digest + b"\n" + plaintext
    return _run_openssl([*OPENSSL_ARGS, "-pass", f"file:{key_path}"], payload)


def decrypt_bytes(ciphertext: bytes, key_path: Path = DEFAULT_KEY_PATH) -> bytes:
    payload = _run_openssl(["-d", *OPENSSL_ARGS, "-pass", f"file:{key_path}"], ciphertext)
    digest, sep, plaintext = payload.partition(b"\n")
    if not sep or hashlib.sha256(plaintext).hexdigest().encode() != digest:
        raise VaultError("checksum mismatch after decrypt: corrupted ciphertext")
    return plaintext


def encrypt_file(src: Path, dest: Path, key_path: Path = DEFAULT_KEY_PATH) -> None:
    dest.write_bytes(encrypt_bytes(src.read_bytes(), key_path))


def decrypt_file(src: Path, dest: Path, key_path: Path = DEFAULT_KEY_PATH) -> None:
    dest.write_bytes(decrypt_bytes(src.read_bytes(), key_path))


def read_maybe_encrypted(path: Path, key_path: Path = DEFAULT_KEY_PATH) -> bytes:
    """path.enc if it exists (decrypted), else path itself, read as plain
    bytes. Lets callers stop caring whether a given file has been migrated
    into the vault yet."""
    enc_path = path.with_name(path.name + ".enc")
    if enc_path.is_file():
        return decrypt_bytes(enc_path.read_bytes(), key_path)
    return path.read_bytes()
