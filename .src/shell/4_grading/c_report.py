from c_exec import Execution


def cat_e(data: bytes) -> str:
    """Render bytes the way `cat -e` would: visible newlines and control chars."""
    out = []
    for byte in data:
        if byte == 0x0A:
            out.append("$\n")
        elif byte == 0x09:
            out.append("^I")
        elif byte < 0x20:
            out.append(f"^{chr(byte + 0x40)}")
        elif byte == 0x7F:
            out.append("^?")
        elif byte < 0x7F:
            out.append(chr(byte))
        else:
            out.append(f"M-{chr(byte - 0x80) if byte >= 0xA0 else '^' + chr(byte - 0x40)}")
    return "".join(out)


def same(expected: Execution, actual: Execution) -> bool:
    if actual.timed_out or actual.crashed or actual.truncated:
        return False
    return (
        expected.stdout == actual.stdout
        and expected.returncode == actual.returncode
    )


_SANITIZER_MARKERS = (
    "ERROR: AddressSanitizer",
    "AddressSanitizer:DEADLYSIGNAL",
    "runtime error:",
    "LeakSanitizer",
)


def sanitizer_excerpt(stderr: bytes) -> str:
    text = stderr.decode("utf-8", "replace")
    for marker in _SANITIZER_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            return text[idx:idx + 1500].strip()
    return ""


def describe_case(argv: list[str], stdin: bytes) -> str:
    shown = " ".join(f'"{a}"' for a in argv) if argv else "(no args)"
    if stdin:
        shown += f"   stdin={stdin!r}"
    return shown


def diff_text(expected: Execution, actual: Execution) -> str:
    report = sanitizer_excerpt(actual.stderr)
    if actual.timed_out:
        return "your program timed out"
    if actual.crashed:
        base = f"your program crashed (signal {actual.signal})"
        return f"{base}\n{report}" if report else base
    if actual.truncated:
        return "your program produced too much output (runaway loop?)"
    lines = [
        "--- expected ---",
        cat_e(expected.stdout),
        "--- your output ---",
        cat_e(actual.stdout),
    ]
    if expected.returncode != actual.returncode:
        lines.append(
            f"exit code: expected {expected.returncode}, got {actual.returncode}"
        )
    if report:
        lines.append("--- sanitizer ---")
        lines.append(report)
    return "\n".join(lines)
