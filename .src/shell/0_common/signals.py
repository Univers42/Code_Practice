import sys
from types import FrameType

from exceptions import ExamInterrupt
from terminal import write_line

try:  # POSIX-only; on other platforms wait_for_enter falls back to safe_input.
    import termios
    import tty
except ImportError:  # pragma: no cover - non-POSIX platforms
    termios = None
    tty = None

MAX_CONSECUTIVE_EOF = 3


def handle_sigint(signum: int, frame: FrameType | None) -> None:
    raise ExamInterrupt()


def _report_interrupt(interrupt_message: str) -> None:
    print()
    if interrupt_message:
        write_line(interrupt_message)


def _count_eof(consecutive_eof: int, interrupt_message: str) -> int:
    consecutive_eof += 1
    if consecutive_eof >= MAX_CONSECUTIVE_EOF:
        write_line("No input available. Closing samushell.")
        exit(0)
    _report_interrupt(interrupt_message)
    return consecutive_eof


def safe_input(
    prompt: str = "", interrupt_message: str = "Use finish to end the exam."
) -> str:
    consecutive_eof = 0
    while True:
        try:
            return input(prompt)
        except ExamInterrupt:
            consecutive_eof = 0
            _report_interrupt(interrupt_message)
        except EOFError:
            consecutive_eof = _count_eof(consecutive_eof, interrupt_message)


def wait_for_enter(interrupt_message: str = "") -> None:
    """Block until the user presses Enter, echoing nothing they type.

    Anything typed before Enter is swallowed silently. Ctrl+D (EOF) and
    Ctrl+C keep the exact semantics of safe_input: three consecutive EOFs
    close the shell, an interrupt just resets the count.
    """
    if termios is None or not sys.stdin.isatty():
        while safe_input(interrupt_message=interrupt_message) != "":
            continue
        return

    fd = sys.stdin.fileno()
    old_attrs = termios.tcgetattr(fd)
    consecutive_eof = 0
    try:
        tty.setcbreak(fd, termios.TCSANOW)
        termios.tcflush(fd, termios.TCIFLUSH)
        while True:
            try:
                char = sys.stdin.read(1)
            except ExamInterrupt:
                consecutive_eof = 0
                _report_interrupt(interrupt_message)
                continue
            if char in ("\n", "\r"):
                return
            if char in ("", "\x04"):
                consecutive_eof = _count_eof(consecutive_eof, interrupt_message)
            else:
                consecutive_eof = 0
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_attrs)
