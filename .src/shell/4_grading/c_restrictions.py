import subprocess
from pathlib import Path

ALLOWED_LINE_PREFIX = "Allowed functions:"

# Compiled in with -fno-stack-protector to avoid this in the first place;
# kept as a belt-and-braces filter in case some toolchain injects it anyway.
_COMPILER_INJECTED = {
    "__stack_chk_fail",
    "__stack_chk_fail_local",
    "__stack_chk_guard",
}


def parse_allowed_functions(subject_path: Path) -> set[str]:
    """rank02 subjects list a whitelist ("Allowed functions: write, malloc"),
    the opposite of rank03/04's blacklist. Empty / "None" / "-" means the
    exercise may not call anything external at all."""
    text = subject_path.read_text()
    for line in text.splitlines():
        if not line.startswith(ALLOWED_LINE_PREFIX):
            continue
        rest = line[len(ALLOWED_LINE_PREFIX):].strip()
        if not rest or rest.lower() in ("none", "none specified", "-"):
            return set()
        names = set()
        for item in rest.split(","):
            name = item.strip().removesuffix("()").strip()
            if name:
                names.add(name)
        return names
    return set()


def _symbols(obj_path: Path) -> tuple[set[str], set[str]]:
    """(defined, undefined) global symbol names for one object file."""
    proc = subprocess.run(
        ["nm", "-P", str(obj_path)], capture_output=True, text=True
    )
    defined: set[str] = set()
    undefined: set[str] = set()
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        name, kind = parts[0], parts[1]
        if kind == "U":
            undefined.add(name)
        elif kind not in ("N", "a"):
            defined.add(name)
    return defined, undefined


def used_external_functions(object_files: list[Path]) -> set[str]:
    """Symbols one of the given object files calls that none of the others
    (i.e. the same submission) define: real external calls (libc & co),
    with symbols the compiler injects on its own filtered out."""
    all_defined: set[str] = set()
    all_undefined: set[str] = set()
    for obj in object_files:
        defined, undefined = _symbols(obj)
        all_defined |= defined
        all_undefined |= undefined
    return (all_undefined - all_defined) - _COMPILER_INJECTED


def forbidden_functions_used(
    object_files: list[Path], allowed: set[str]
) -> list[str]:
    return sorted(used_external_functions(object_files) - allowed)
