import readline  # noqa: F401 - enables arrow-key history for input()

from clock import format_remaining_time, get_remaining_time, start_exam_clock
from constants import EXERCISE_NAMES, PROMPT, colored
from exercises import pick_random_exercise
from filesystem import copy_subject, prepare_exam_directories
from signals import safe_input
from terminal import clear_screen, write_line


def print_status(
    level: int, score: int, exercise: int, exam_deadline: float
) -> None:
    name = EXERCISE_NAMES[exercise]
    remaining = format_remaining_time(get_remaining_time(exam_deadline))
    print(f"Actual exercise: {colored(f'{level}/4', 'green')} {name}. ",
          end="")
    print(f"Subject aviable in subject/{name}.txt")
    print(f"Actual score: {colored(f'{score}/100', 'green')}")
    print(colored("25 point aviables in current exercise.", "green"))
    print(colored(remaining, "green"))


def print_commands() -> None:
    write_line("Available commands:")
    write_line(
        f"{colored('grademe', 'green')}: to evaluate your current exercise."
    )
    write_line(
        f"{colored('status', 'green')}: to show your current status."
    )
    write_line(
            f"{colored('clear', 'green')}: clear the samushell terminal."
        )
    write_line(f"{colored('finish', 'green')}: to finish your exam.")


def start_exam(exercises: list[int]) -> None:
    clear_screen()
    write_line("Enter your login: ", end="")
    login = safe_input()
    write_line(f"Loading the current exam from the student {login}...",
               wait=1)

    write_line(f"You have {colored('1', 'green')} exam aviable.", wait=2)
    write_line("You are entring in the real exam mode.")
    write_line(
        f"You have {colored('3 hours', 'green')} remainig "
        "for finish yours exercices."
    )
    print_commands()
    write_line(colored("Press [ENTER] to start:", "gray"), end="")
    while safe_input() != "":
        continue
    prepare_exam_directories()
    exam_deadline = start_exam_clock(hours=3)
    level = 1
    score = 0
    exercise = pick_random_exercise(exercises)
    copy_subject(exercise)
    print_status(level, score, exercise, exam_deadline)
    command = safe_input(PROMPT)
    while command != "finish":
        if command == "status":
            print_status(level, score, exercise, exam_deadline)
            print_commands()
        elif command == "grademe":
            pass
        elif command == "finish":
            break
        elif command == "clear":
            clear_screen()
        else:
            print("Unreconiced command. Type 'status' for more information.")

        command = safe_input(PROMPT)
