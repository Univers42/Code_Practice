from constants import PROMPT
from exam import practice_exercise, start_exam
from exam_config import ExamConfig, get_exam_config
from signals import safe_input
from terminal import clear_screen, write_line


def show_all_exercises(config: ExamConfig) -> None:
    while True:
        clear_screen()
        write_line(f"All exercises (Rank {config.rank:02d}):")
        for number, name in enumerate(config.exercise_names, start=1):
            write_line(f"[{number}] {name}")
        write_line("[q] Back")
        choice = safe_input(PROMPT)
        if choice == "q":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(config.exercise_names):
            practice_exercise(config, int(choice) - 1)


def show_exam_menu(config: ExamConfig) -> None:
    while True:
        clear_screen()
        write_line(f"Rank {config.rank:02d}")
        write_line("[1] Start exam")
        write_line("[2] Show all exercises")
        write_line("[q] Back")
        choice = safe_input(PROMPT)
        if choice == "1":
            start_exam(config)
            exit(0)
        elif choice == "2":
            show_all_exercises(config)
        elif choice == "q":
            return


def show_main_menu() -> None:
    while True:
        clear_screen()
        write_line("Welcome to samushell", 2)
        write_line("[1] Rank 03")
        write_line("[2] Rank 04")
        write_line("[3] Exit")
        choice = safe_input(PROMPT)
        if choice == "1":
            show_exam_menu(get_exam_config(3))
        elif choice == "2":
            show_exam_menu(get_exam_config(4))
        elif choice == "3":
            clear_screen()
            exit(0)
