import random
import time

from clock import format_remaining_time, get_remaining_time, start_exam_clock
from constants import PROMPT, colored
from cooldown import format_cooldown, get_remaining_cooldown
from exam_config import ExamConfig
from exercises import pick_exam_exercise
from filesystem import copy_statement, prepare_exam_directories
from shared import statement_files_message
from signals import safe_input, wait_for_enter
from terminal import clear_screen, write_line
from testing import choice_test


def confirm(question: str) -> bool:
    prompt = f"{colored(question, 'red')} (y/n): "
    while True:
        answer = safe_input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"


def grading_wait_pauses() -> list[float]:
    count = random.randint(1, 3)
    if count == 1:
        return [random.uniform(5, 6)]
    while True:
        pauses = [random.uniform(2, 4) for _ in range(count)]
        if sum(pauses) >= 5:
            return pauses


def simulate_grading_delay() -> None:
    print(colored(
        "10 seconds is fast. 3 minutes is slow. 30 seconds is expected.",
        "green",
    ))
    for pause in grading_wait_pauses():
        write_line(colored("compiling...", "white"), pause)


def trace_file_message(config: ExamConfig) -> str:
    filename = (
        f"{config.level}_{config.retrys}_traces_{config.current_exercise}.txt"
    )
    return f"Traces for {config.current_exercise} saved in traces/{filename}"


def print_status(
    config: ExamConfig,
    level: int,
    score: int,
    exercise: int,
    exam_deadline: float,
) -> None:
    name = config.exercise_names[exercise]
    remaining = format_remaining_time(get_remaining_time(exam_deadline))
    available = config.points_for_level(level)
    print(
        f"Actual exercise: "
        f"{colored(f'{level}/{config.last_level}', 'green')} "
        f"{name}. ",
        end="",
    )
    print(statement_files_message(name))
    print(f"Actual score: {colored(f'{score}/100', 'green')}")
    print(colored(
        f"{available} points available in current exercise.", "green"
    ))
    print(colored(remaining, "green"))


def print_commands() -> None:
    write_line("Available commands:")
    write_line(
        f"{colored('evaluate', 'green')}: to evaluate your current exercise."
    )
    write_line(
        f"{colored('show', 'green')}: to show your current status."
    )
    write_line(
            f"{colored('clear', 'green')}: clear the samushell terminal."
        )
    write_line(f"{colored('exit', 'green')}: to finish your exam.")


def start_exam(config: ExamConfig) -> None:
    exercises = config.exercise_pool()
    clear_screen()
    write_line("Enter your name: ", end="")
    name = safe_input().strip() or "Mr. Anonymous"
    write_line(f"Welcome, {name}.", wait=1)

    write_line(f"You have {colored('1', 'green')} exam available.", wait=2)
    write_line("You are entering the real exam mode.")
    write_line(
        f"You have {colored('3 hours', 'green')} remaining "
        "to finish your exercises."
    )
    print_commands()
    write_line(colored("Press [ENTER] to start:\n", "gray"), end="")
    wait_for_enter()
    prepare_exam_directories()
    exam_deadline = start_exam_clock(hours=3)
    exam_start = time.time()
    level = 0
    score = 0
    exercise = pick_exam_exercise(config.rank, level, exercises)
    copy_statement(config, exercise)
    print_status(config, level, score, exercise, exam_deadline)
    command = safe_input(PROMPT)
    while command != "exit":
        if get_remaining_time(exam_deadline) <= 0:
            print(colored("Time's up! Your exam has ended.", "red"))
            print(f"Final score: {colored(f'{score}/100', 'green')}")
            break
        if command == "show":
            print_status(config, level, score, exercise, exam_deadline)
            print_commands()
        elif command == "evaluate":
            if confirm("Are you completely sure?"):
                remaining_cooldown = get_remaining_cooldown(
                    config.last_failure_time, config.retrys
                )
                if remaining_cooldown > 0:
                    wait_time = colored(
                        format_cooldown(remaining_cooldown), "yellow"
                    )
                    print(
                        f"You must wait {wait_time} "
                        "to try again. Be patient."
                    )
                    write_line(
                        colored("Press [ENTER] to continue:\n", "gray"), end=""
                    )
                    wait_for_enter()
                    command = safe_input(PROMPT)
                    continue
                simulate_grading_delay()
                config.level = level
                result = choice_test(config)
                if result[-1]:
                    print(
                        colored(">>>>>PASSED<<<<<", "green")
                    )
                    write_line(
                        colored("Press [ENTER] to continue:\n", "gray"), end=""
                    )
                    wait_for_enter()
                    level += 1
                    config.retrys = 0
                    config.last_failure_time = 0.0
                    score = config.score_after(level)
                    if level > config.last_level:
                        break
                    exercise = pick_exam_exercise(config.rank, level, exercises)
                    copy_statement(config, exercise)
                    print_status(config, level, score, exercise, exam_deadline)
                else:
                    config.last_failure_time = time.time()
                    print(
                            colored(">>>>>FAILURE<<<<<", "red")
                        )
                    print(trace_file_message(config))
                    write_line(
                        colored("Press [ENTER] to retry:\n", "gray"), end=""
                        )
                    wait_for_enter()
                    config.retrys += 1
                    command = safe_input(PROMPT)
                    continue
        elif command == "exit":
            break
        elif command == "clear":
            clear_screen()
        else:
            print("Unrecognized command. Type 'show' for more information.")

        command = safe_input(PROMPT)
    if level > config.last_level:
        level = config.last_level
    write_line(
        f"You reached exercise "
        f"{colored(f'{level}/{config.last_level}', 'green')}", 2
    )
    if score == 100:
        write_line(
                colored("You reached max score!", "green"), 2
            )
        elapsed = format_remaining_time(time.time() - exam_start)
        write_line(colored(f"Exam completed in {elapsed}", "green"), 2)
