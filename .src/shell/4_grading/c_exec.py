import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

RUN_TIMEOUT = 5.0
OUTPUT_CAP = 1 << 20  # 1 MiB; anything past this is treated as a runaway

# Make a sanitizer hit abort immediately with its report on stderr. Harmless
# for the (unsanitized) reference binary, which just ignores these.
_SANITIZER_ENV = {
    "ASAN_OPTIONS": "abort_on_error=1:detect_leaks=0",
    "UBSAN_OPTIONS": "print_stacktrace=1:halt_on_error=1",
}


@dataclass
class Execution:
    stdout: bytes
    stderr: bytes
    returncode: int
    timed_out: bool
    truncated: bool

    @property
    def crashed(self) -> bool:
        return self.returncode < 0

    @property
    def signal(self) -> int:
        return -self.returncode if self.returncode < 0 else 0


def run_binary(
    binary: Path,
    argv: list[str],
    stdin: bytes = b"",
    timeout: float = RUN_TIMEOUT,
) -> Execution:
    try:
        proc = subprocess.run(
            [str(binary), *argv],
            input=stdin,
            capture_output=True,
            cwd=binary.parent,
            timeout=timeout,
            env={**os.environ, **_SANITIZER_ENV},
        )
    except subprocess.TimeoutExpired as expired:
        partial = expired.stdout or b""
        return Execution(
            partial[:OUTPUT_CAP], b"", 0, True, len(partial) > OUTPUT_CAP
        )

    out = proc.stdout or b""
    return Execution(
        out[:OUTPUT_CAP],
        proc.stderr or b"",
        proc.returncode,
        False,
        len(out) > OUTPUT_CAP,
    )
