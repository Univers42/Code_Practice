import subprocess
from dataclasses import dataclass
from pathlib import Path

CFLAGS = ["-Wall", "-Wextra", "-Werror"]
# Applied to the student's build only: catches heap overflows, missing NULL
# terminators, use-after-free, signed overflow and out-of-range shifts.
SANITIZE_FLAGS = [
    "-fsanitize=address,undefined",
    "-fno-omit-frame-pointer",
    "-g",
]
COMPILE_TIMEOUT = 30.0


@dataclass
class CompileResult:
    ok: bool
    command: str
    log: str


def compile_binary(
    work_dir: Path,
    sources: list[str],
    output: str,
    extra_flags: list[str] | None = None,
) -> CompileResult:
    """Compile `sources` (filenames relative to work_dir) into work_dir/output.

    Everything runs with cwd=work_dir so that `#include "super.h"` and the
    per-exercise headers copied next to the sources resolve without -I.
    """
    command = ["cc", *CFLAGS, *(extra_flags or []), *sources, "-o", output]
    printable = " ".join(command)
    try:
        proc = subprocess.run(
            command,
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=COMPILE_TIMEOUT,
        )
    except FileNotFoundError:
        return CompileResult(False, printable, "cc not found")
    except subprocess.TimeoutExpired:
        return CompileResult(False, printable, "compilation timed out")

    log = (proc.stdout or "") + (proc.stderr or "")
    return CompileResult(proc.returncode == 0, printable, log.strip())


def compile_object(work_dir: Path, source: str) -> tuple[CompileResult, Path]:
    """Compile one source to a .o, no sanitizer instrumentation and no
    stack-protector symbol, so nm sees only what the source itself calls.
    Used for the allowed-functions check, not for grading execution."""
    obj_name = Path(source).stem + ".o"
    result = compile_binary(
        work_dir, [source], obj_name, extra_flags=["-c", "-fno-stack-protector"]
    )
    return result, work_dir / obj_name
