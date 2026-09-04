import pathsetup  # noqa: F401 - adds sibling module directories to sys.path

import atexit
import signal

import readline  # noqa: F401 - enables arrow-key history for input()

from exam_config import validate_rank_data
from filesystem import cleanup_statement_dir, cleanup_traces_dir
from menu import show_main_menu
from signals import handle_sigint

if __name__ == "__main__":
    problems = validate_rank_data()
    if problems:
        for problem in problems:
            print(problem)
        raise SystemExit(1)
    signal.signal(signal.SIGINT, handle_sigint)
    atexit.register(cleanup_statement_dir)
    atexit.register(cleanup_traces_dir)
    show_main_menu()
