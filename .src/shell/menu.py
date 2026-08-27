from constants import (
    LEVELS_BY_RANK,
    PROMPT,
    bracket_option,
    colored,
    separator_line,
    underlined_header,
)
from exam import practice_exercise, start_exam
from exam_config import ExamConfig, get_exam_config
from signals import safe_input
from terminal import clear_screen, write_line


def show_all_exercises(config: ExamConfig) -> None:
    while True:
        clear_screen()
        header = f"All exercises (Rank {config.rank:02d}):"
        write_line(colored(header, "green"))
        write_line(separator_line())
        number = 1
        for level_name, names in LEVELS_BY_RANK[config.rank]:
            write_line(underlined_header(level_name))
            for name in names:
                write_line(bracket_option(str(number), name))
                number += 1
        write_line(separator_line())
        write_line(bracket_option("q", "Back"))
        write_line(bracket_option("exit", "Close @samushell"))
        write_line(separator_line())
        choice = safe_input(PROMPT, interrupt_message="")
        if choice == "q":
            return
        if choice == "exit":
            clear_screen()
            exit(0)
        if choice.isdigit() and 1 <= int(choice) <= len(config.exercise_names):
            practice_exercise(config, int(choice) - 1)


def show_exam_menu(config: ExamConfig) -> None:
    while True:
        clear_screen()
        write_line(colored(f"Rank {config.rank:02d}", "green"))
        write_line(separator_line())
        write_line(bracket_option("1", "Start exam"))
        write_line(bracket_option("2", "Show all exercises"))
        write_line(bracket_option("q", "Back"))
        write_line(bracket_option("exit", "Close @samushell"))
        write_line(separator_line())
        choice = safe_input(PROMPT, interrupt_message="")
        if choice == "1":
            start_exam(config)
            exit(0)
        elif choice == "2":
            show_all_exercises(config)
        elif choice == "q":
            return
        elif choice == "exit":
            clear_screen()
            exit(0)


def show_main_menu() -> None:
    while True:
        clear_screen()
        write_line(colored("Welcome to samushell", "green"), 2)
        write_line(separator_line())
        write_line(bracket_option("3", "Rank 03"))
        write_line(bracket_option("4", "Rank 04"))
        write_line(bracket_option("q", "Exit"))
        write_line(separator_line())
        choice = safe_input(PROMPT, interrupt_message="")
        if choice == "3":
            show_exam_menu(get_exam_config(3))
        elif choice == "4":
            show_exam_menu(get_exam_config(4))
        elif choice == "q":
            clear_screen()
            exit(0)
