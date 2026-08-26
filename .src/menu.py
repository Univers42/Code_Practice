from constants import EXERCISE_NAMES, PROMPT
from exam import start_exam
from signals import safe_input
from terminal import clear_screen, write_line


def show_all_exercises(exercises: list[int]) -> None:
    while True:
        clear_screen()
        write_line("All exercises:")
        for number, name in enumerate(EXERCISE_NAMES, start=1):
            write_line(f"[{number}] {name}")
        write_line("[q] Back")
        choice = safe_input(PROMPT)
        if choice == "q":
            return


def show_main_menu(exercises: list[int]) -> None:
    while True:
        clear_screen()
        write_line("Welcome to samushell")
        write_line("[1] Start exam")
        write_line("[2] Show all exercises")
        write_line("[3] Exit")
        choice = safe_input(PROMPT)
        if choice == "1":
            start_exam(exercises)
            exit(0)
        elif choice == "2":
            show_all_exercises(exercises)
        elif choice == "3":
            clear_screen()
            exit(0)
