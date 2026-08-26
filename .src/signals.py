from terminal import write_line


class ExamInterrupt(Exception):
    pass


def handle_sigint(signum, frame) -> None:
    raise ExamInterrupt()


def safe_input(prompt: str = "") -> str:
    while True:
        try:
            return input(prompt)
        except ExamInterrupt:
            print()
            write_line("Use finish for end the exam.")
