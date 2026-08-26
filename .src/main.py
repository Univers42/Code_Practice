import atexit
import signal

from filesystem import cleanup_subject_dir
from menu import show_main_menu
from signals import handle_sigint

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_sigint)
    atexit.register(cleanup_subject_dir)
    exercises: list[int] = [0, 1, 2, 3, 4, 5, 6]
    show_main_menu(exercises)
