from terminal import write_line


class ExamInterrupt(Exception):
    pass


def handle_sigint(signum, frame) -> None:
    raise ExamInterrupt()


def safe_input(prompt: str = "") -> str:
    while True:
        try:
            return input(prompt)
        except (ExamInterrupt, EOFError):
            print()
            write_line("Use finish to end the exam.")
