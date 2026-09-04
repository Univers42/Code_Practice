import shutil
from pathlib import Path

from c_vault import decrypt_bytes
from exam_config import ExamConfig


def recreate_dir(path: str) -> None:
    dir_path = Path(path)
    if dir_path.exists():
        shutil.rmtree(dir_path)
    dir_path.mkdir(parents=True)


def prepare_exam_directories() -> None:
    recreate_dir("projects")
    recreate_dir("statement")


def ensure_projects_dir() -> None:
    Path("projects").mkdir(exist_ok=True)


def copy_statement(config: ExamConfig, exercise: int) -> None:
    name = config.exercise_names[exercise]
    config.current_exercise = name
    source = Path(config.statements_dir) / name
    destination = Path("statement") / name
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    for item in source.iterdir():
        if item.suffix == ".enc":
            plain_name = item.name.removesuffix(".enc")
            (destination / plain_name).write_bytes(decrypt_bytes(item.read_bytes()))
        else:
            shutil.copy(item, destination / item.name)
    ensure_projects_dir()


def cleanup_statement_dir() -> None:
    statement_dir = Path("statement")
    if statement_dir.exists():
        shutil.rmtree(statement_dir)


def cleanup_traces_dir() -> None:
    traces_dir = Path("traces")
    if traces_dir.exists():
        shutil.rmtree(traces_dir)
