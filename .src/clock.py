import time


def start_exam_clock(hours: int = 3,
                     minutes: int = 0,
                     seconds: int = 0) -> float:
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return time.time() + total_seconds


def get_remaining_time(deadline: float) -> float:
    return deadline - time.time()


def format_remaining_time(seconds: float) -> str:
    total_seconds = max(0, int(seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
