import math
import time

BASE_SECONDS = 30
GROWTH_EXPONENT = math.log(20, 5)


def cooldown_duration(retrys: int) -> float:
    if retrys <= 0:
        return 0.0
    return BASE_SECONDS * math.pow(retrys, GROWTH_EXPONENT)


def get_remaining_cooldown(last_failure_time: float, retrys: int) -> float:
    if retrys <= 0 or last_failure_time <= 0:
        return 0.0
    elapsed = time.time() - last_failure_time
    return max(0.0, cooldown_duration(retrys) - elapsed)


def format_cooldown(seconds: float) -> str:
    total = max(0, math.ceil(seconds - 1e-9))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes}m {secs}s"
    if minutes:
        return f"{minutes}m {secs}s"
    return f"{secs}s"
