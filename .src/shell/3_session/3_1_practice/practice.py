import random
from pathlib import Path

from constants import PROMPT, colored
from exam_config import ExamConfig
from filesystem import copy_statement
from shared import statement_files_message
from signals import safe_input, wait_for_enter
from terminal import clear_screen, write_line
from testing import choice_test


def print_practice_commands() -> None:
    write_line("Available commands:")
    write_line(
        f"{colored('evaluate', 'green')}: to evaluate your current exercise."
    )
    write_line(
        f"{colored('show', 'green')}: to show your current status."
    )
    write_line(
        f"{colored('statement', 'green')}: to print the exercise statement."
    )
    write_line(
        f"{colored('next', 'green')}: to move to the next exercise."
    )
    write_line(
        f"{colored('clear', 'green')}: clear the samushell terminal."
    )
    write_line(f"{colored('exit', 'green')}: to finish your exam.")


def print_practice_status(name: str) -> None:
    print(f"Actual exercise: {colored(name, 'green')}")
    print(statement_files_message(name))
    print_practice_commands()


def print_statement(name: str) -> None:
    statement_path = Path("statement") / name / "statement.en.txt"
    try:
        print(statement_path.read_text())
    except OSError as error:
        print(f"ERROR: could not read the statement file: {error}")


def practice_exercise(config: ExamConfig, exercise: int) -> None:
    while True:
        copy_statement(config, exercise)
        clear_screen()
        name = config.exercise_names[exercise]
        print_practice_status(name)
        command = safe_input(PROMPT)
        next_exercise = -1
        while command != "exit" and next_exercise == -1:
            if command == "evaluate":
                result = choice_test(config)
                if result[-1]:
                    print(
                            colored(">>>>>PASSED<<<<<", "green")
                        )
                    write_line(
                        colored("Press [ENTER] to go back:\n", "gray"),
                        end="",
                        )
                    wait_for_enter()
                    return
                else:
                    print(
                            colored(">>>>>FAILURE<<<<<", "red")
                        )
                    write_line(
                        colored("Press [ENTER] to retry:\n", "gray"), end=""
                        )
                    wait_for_enter()
                    config.retrys += 1
                    command = safe_input(PROMPT)
                    continue
            elif command == "show":
                print_practice_status(name)
            elif command == "statement":
                print_statement(name)
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
                    "Unrecognized command. Type 'show' for more"
                    " information."
                )

            command = safe_input(PROMPT)
        if command == "exit":
            return
        exercise = next_exercise
