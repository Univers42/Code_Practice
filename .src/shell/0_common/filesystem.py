import shutil
from pathlib import Path

from exam_config import ExamConfig


def recreate_dir(path: str) -> None:
    dir_path = Path(path)
    if dir_path.exists():
        shutil.rmtree(dir_path)
    dir_path.mkdir(parents=True)


def prepare_exam_directories() -> None:
    recreate_dir("rendu")
    recreate_dir("subject")


def ensure_rendu_dir() -> None:
    Path("rendu").mkdir(exist_ok=True)


def copy_subject(config: ExamConfig, exercise: int) -> None:
    name = config.exercise_names[exercise]
    config.current_exercise = name
    destination = Path("subject") / name
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(f"{config.subjects_dir}/{name}", destination)
    ensure_rendu_dir()


def cleanup_subject_dir() -> None:
    subject_dir = Path("subject")
    if subject_dir.exists():
        shutil.rmtree(subject_dir)


def cleanup_traces_dir() -> None:
    traces_dir = Path("traces")
    if traces_dir.exists():
        shutil.rmtree(traces_dir)
