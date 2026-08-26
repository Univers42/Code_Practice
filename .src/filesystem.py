import shutil
from pathlib import Path

from constants import EXERCISE_NAMES


def recreate_dir(path: str) -> None:
    dir_path = Path(path)
    if dir_path.exists():
        shutil.rmtree(dir_path)
    dir_path.mkdir(parents=True)


def prepare_exam_directories() -> None:
    recreate_dir("rendu")
    recreate_dir("subject")


def copy_subject(exercise: int) -> None:
    name = EXERCISE_NAMES[exercise]
    destination = Path("subject") / name
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(f".subjects/{name}", destination)


def cleanup_subject_dir() -> None:
    subject_dir = Path("subject")
    if subject_dir.exists():
        shutil.rmtree(subject_dir)
