import time

from exceptions import ExamInterrupt


def clear_screen() -> None:
    print("\033[3J\033[H\033[2J", end="")


def write_line(text: str, wait: float = 0, end: str = "\n") -> None:
    print(text, end=end, flush=True)
    try:
        time.sleep(wait)
    except ExamInterrupt:
        pass
