import atexit
import signal

from filesystem import cleanup_subject_dir, prepare_exam_directories
from menu import show_main_menu
from signals import handle_sigint

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_sigint)
    atexit.register(cleanup_subject_dir)
    prepare_exam_directories()
    show_main_menu()
