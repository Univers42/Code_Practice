import readline  # noqa: F401 - enables arrow-key history for input()

from clock import format_remaining_time, get_remaining_time, start_exam_clock
from constants import EXERCISE_NAMES, PROMPT, colored
from exercises import pick_random_exercise
from filesystem import copy_subject, prepare_exam_directories
from signals import safe_input
from terminal import clear_screen, write_line


def subject_files_message(name: str) -> str:
    return f"Subject available in subject/{name}/"


def confirm(question: str) -> bool:
    prompt = f"{colored(question, 'red')} (y/n): "
    while True:
        answer = safe_input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"


def print_status(
    level: int, score: int, exercise: int, exam_deadline: float
) -> None:
    name = EXERCISE_NAMES[exercise]
    remaining = format_remaining_time(get_remaining_time(exam_deadline))
    print(f"Actual exercise: {colored(f'{level}/4', 'green')} {name}. ",
          end="")
    print(subject_files_message(name))
    print(f"Actual score: {colored(f'{score}/100', 'green')}")
    print(colored("25 points available in current exercise.", "green"))
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


def print_practice_commands() -> None:
    write_line("Available commands:")
    write_line(
        f"{colored('grademe', 'green')}: to evaluate your current exercise."
    )
    write_line(
        f"{colored('clear', 'green')}: clear the samushell terminal."
    )
    write_line(f"{colored('finish', 'green')}: to finish your exam.")


def practice_exercise(exercise: int) -> None:
    copy_subject(exercise)
    clear_screen()
    name = EXERCISE_NAMES[exercise]
    print(f"Actual exercise: {colored(name, 'green')}")
    print(subject_files_message(name))
    print_practice_commands()
    command = safe_input(PROMPT)
    while command != "finish":
        if command == "grademe":
            pass
        elif command == "clear":
            clear_screen()
        else:
            print("Unrecognized command. Type 'grademe' or 'finish'.")

        command = safe_input(PROMPT)


def start_exam(exercises: list[int]) -> None:
    clear_screen()
    write_line("Enter your login: ", end="")
    login = safe_input()
    write_line(f"Loading the current exam from the student {login}...",
               wait=1)

    write_line(f"You have {colored('1', 'green')} exam available.", wait=2)
    write_line("You are entering in the real exam mode.")
    write_line(
        f"You have {colored('3 hours', 'green')} remaining "
        "to finish your exercises."
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
    while command != "finish" or level > 4:
        if get_remaining_time(exam_deadline) <= 0:
            print(colored("Time's up! Your exam has ended.", "red"))
            print(f"Final score: {colored(f'{score}/100', 'green')}")
            break
        if command == "status":
            print_status(level, score, exercise, exam_deadline)
            print_commands()
        elif command == "grademe":
            if confirm("Are you completely sure?"):
                print(
                    colored(">>>>>PASSED<<<<<", "green")
                )
                write_line(
                    colored("Press [ENTER] to continue:", "gray"), end=""
                )
                while safe_input() != "":
                    continue
                level += 1
                score += 25
                if level <= 4:
                    exercise = pick_random_exercise(exercises)
                    copy_subject(exercise)
                    print_status(level, score, exercise, exam_deadline)
        elif command == "finish":
            break
        elif command == "clear":
            clear_screen()
        else:
            print("Unrecognized command. Type 'status' for more information.")

        command = safe_input(PROMPT)
    if level > 4:
        level = 4
    write_line(
        f"You reach at excersice {colored(f"{level}/4", 'green')}", 2
    )
    if score == 100:
        write_line(
                colored("You reach max score!", "green"), 2
            )
