from types import FrameType

from exceptions import ExamInterrupt
from terminal import write_line

MAX_CONSECUTIVE_EOF = 3


def handle_sigint(signum: int, frame: FrameType | None) -> None:
    raise ExamInterrupt()


def safe_input(
    prompt: str = "", interrupt_message: str = "Use finish to end the exam."
) -> str:
    consecutive_eof = 0
    while True:
        try:
            return input(prompt)
        except ExamInterrupt:
            consecutive_eof = 0
            print()
            if interrupt_message:
                write_line(interrupt_message)
        except EOFError:
            consecutive_eof += 1
            if consecutive_eof >= MAX_CONSECUTIVE_EOF:
                write_line("No input available. Closing samushell.")
                exit(0)
            print()
            if interrupt_message:
                write_line(interrupt_message)
