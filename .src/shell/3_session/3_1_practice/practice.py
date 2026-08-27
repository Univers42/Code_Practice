import random
from pathlib import Path

from constants import PROMPT, colored
from exam_config import ExamConfig
from filesystem import copy_subject
from shared import subject_files_message
from signals import safe_input
from terminal import clear_screen, write_line
from testing import choice_test


def print_practice_commands() -> None:
    write_line("Available commands:")
    write_line(
        f"{colored('grademe', 'green')}: to evaluate your current exercise."
    )
    write_line(
        f"{colored('status', 'green')}: to show your current status."
    )
    write_line(
        f"{colored('subject', 'green')}: to print the exercise subject."
    )
    write_line(
        f"{colored('next', 'green')}: to move to the next exercise."
    )
    write_line(
        f"{colored('clear', 'green')}: clear the samushell terminal."
    )
    write_line(f"{colored('finish', 'green')}: to finish your exam.")


def print_practice_status(name: str) -> None:
    print(f"Actual exercise: {colored(name, 'green')}")
    print(subject_files_message(name))
    print_practice_commands()


def print_subject(name: str) -> None:
    subject_path = Path("subject") / name / "subject.en.txt"
    try:
        print(subject_path.read_text())
    except OSError as error:
        print(f"ERROR: could not read the subject file: {error}")


def practice_exercise(config: ExamConfig, exercise: int) -> None:
    while True:
        copy_subject(config, exercise)
        clear_screen()
        name = config.exercise_names[exercise]
        print_practice_status(name)
        command = safe_input(PROMPT)
        next_exercise = -1
        while command != "finish" and next_exercise == -1:
            if command == "grademe":
                result = choice_test(config)
                if result[-1]:
                    print(
                            colored(">>>>>PASSED<<<<<", "green")
                        )
                    write_line(
                        colored("Press [ENTER] to go back:\n", "gray"),
                        end="",
                        )
                    while safe_input() != "":
                        continue
                    return
                else:
                    print(
                            colored(">>>>>FAILURE<<<<<", "red")
                        )
                    write_line(
                        colored("Press [ENTER] to retry:\n", "gray"), end=""
                        )
                    while safe_input() != "":
                        continue
                    config.retrys += 1
                    command = safe_input(PROMPT)
                    continue
            elif command == "status":
                print_practice_status(name)
            elif command == "subject":
                print_subject(name)
            elif command == "next":
                pool_size = len(config.exercise_names)
                next_exercise = exercise
                while next_exercise == exercise and pool_size > 1:
                    next_exercise = random.randrange(pool_size)
                continue
            elif command == "clear":
                clear_screen()
            else:
                print(
                    "Unrecognized command. Type 'status' for more"
                    " information."
                )

            command = safe_input(PROMPT)
        if command == "finish":
            return
        exercise = next_exercise
