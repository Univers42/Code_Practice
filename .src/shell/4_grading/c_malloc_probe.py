import os
import subprocess
from pathlib import Path

RANK02_SRC = Path(__file__).resolve().parents[3] / ".src" / "rank02"
PROBE_SRC = RANK02_SRC / "malloc_probe.c"
PROBE_TIMEOUT = 30.0
RUN_TIMEOUT = 5.0

# A single-position slack: an allocation is fine as long as it's within a
# small multiple of what was actually needed, plus a flat few bytes of
# margin for things like alignment or a "+1 for luck". This has to be a
# TIGHT bound, not a generous one — a big multiplier (8x, 10x) would let
# "just use strlen() of the whole input as a safe size" slip through
# whenever the input isn't dramatically longer than the item in question.
SLACK_MULT = 3
SLACK_ADD = 16


def build_probe(work_dir: Path) -> Path | None:
    so_path = work_dir / "malloc_probe.so"
    try:
        proc = subprocess.run(
            ["cc", "-shared", "-fPIC", "-O0", str(PROBE_SRC), "-o", str(so_path), "-ldl"],
            capture_output=True, text=True, timeout=PROBE_TIMEOUT,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    return so_path if proc.returncode == 0 else None


def run_with_probe(
    binary: Path, argv: list[str], stdin: bytes, probe_so: Path, log_path: Path
) -> list[int]:
    """Run binary once under the probe; never combine with a sanitized
    binary (-fsanitize=address installs its own allocator and conflicts
    with an LD_PRELOAD malloc hook)."""
    if log_path.exists():
        log_path.unlink()
    env = {**os.environ, "LD_PRELOAD": str(probe_so), "MALLOC_PROBE_LOG": str(log_path)}
    try:
        subprocess.run(
            [str(binary), *argv],
            input=stdin,
            capture_output=True,
            cwd=binary.parent,
            timeout=RUN_TIMEOUT,
            env=env,
        )
    except subprocess.TimeoutExpired:
        pass
    if not log_path.is_file():
        return []
    sizes = []
    for line in log_path.read_text().splitlines():
        line = line.strip()
        if line.isdigit():
            sizes.append(int(line))
    return sizes


def _too_big(observed: int, expected: int) -> bool:
    return observed > SLACK_MULT * expected + SLACK_ADD


def _closest(values: list[int], target: int) -> int | None:
    if not values:
        return None
    return min(values, key=lambda v: abs(v - target))


def subtract_common(observed: list[int], baseline: list[int]) -> list[int]:
    """Multiset difference: drop one occurrence of each size in `observed`
    for every matching occurrence in `baseline`. The reference shares the
    exact same driver (main.c) as the student, so any incidental malloc
    the driver itself triggers (e.g. glibc's first buffered stdio write
    mallocs a ~4KB buffer) shows up identically in both and is not
    something the student's code did — it must not count against them."""
    remaining = list(baseline)
    result = []
    for size in observed:
        if size in remaining:
            remaining.remove(size)
        else:
            result.append(size)
    return result


def _check_single(observed: list[int], expected: int) -> str | None:
    """For exercises with exactly one real buffer to size (ft_strdup,
    ft_itoa, ft_range, ft_rrange). `observed` must already have the
    reference's own incidental allocations subtracted out (see
    subtract_common) — otherwise driver-internal noise bigger than a
    small expected size (e.g. glibc's stdio buffer) reads as "the buffer"."""
    if not observed:
        return None
    biggest = max(observed)
    if _too_big(biggest, expected):
        return f"allocated {biggest} bytes for something that needed ~{expected}"
    return None


def _check_split(argv: list[str], observed: list[int]) -> str | None:
    words = argv[0].split() if argv else []
    if not words or not observed:
        return None
    word_sizes = sorted(len(w) + 1 for w in words)
    array_size = 8 * (len(words) + 1)
    remaining = list(observed)
    match = _closest(remaining, array_size)
    if match is not None and abs(match - array_size) <= max(16, array_size // 2):
        remaining.remove(match)
    word_observed = sorted(remaining)
    for exp, obs in zip(word_sizes, word_observed):
        if _too_big(obs, exp):
            return f"reserved {obs} bytes for a word that only needed ~{exp}"
    return None


# name -> (expected_sizes_fn | "split", probe_argv_cases)
# probe_argv_cases are extra, dedicated argv lists (on top of the normal
# TEST_CASES) chosen so a "just use one big/uniform size" cheat is exposed:
# a tiny item sitting next to a much bigger one in the SAME call, so a
# single global bound looks absurd against the tiny one specifically.
MALLOC_CHECKS: dict[str, tuple] = {
    "ft_strdup": (lambda argv: len(argv[0]) + 1, [["a"], ["a" + "x" * 500]]),
    "ft_itoa": (lambda argv: len(str(int(argv[0]))) + 1, [["1"], ["-2147483648"]]),
    "ft_range": (
        lambda argv: 4 * (abs(int(argv[1]) - int(argv[0])) + 1),
        [["1", "1"], ["1", "500"]],
    ),
    "ft_rrange": (
        lambda argv: 4 * (abs(int(argv[1]) - int(argv[0])) + 1),
        [["1", "1"], ["1", "500"]],
    ),
    "ft_split": (
        "split",
        [["a " + "x" * 300], ["a bb ccc " + "x" * 300]],
    ),
}


def check_allocations(
    exercise: str, argv: list[str], observed: list[int], baseline: list[int]
) -> str | None:
    entry = MALLOC_CHECKS.get(exercise)
    if entry is None:
        return None
    observed = subtract_common(observed, baseline)
    expected_fn, _ = entry
    if expected_fn == "split":
        return _check_split(argv, observed)
    try:
        expected = expected_fn(argv)
    except (ValueError, IndexError):
        return None
    return _check_single(observed, expected)
