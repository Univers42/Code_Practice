import ast
from pathlib import Path

FORBIDDEN_LINE_PREFIX = "Forbidden functions:"


def parse_forbidden_functions(subject_path: Path) -> list[str]:
    text = subject_path.read_text()
    for line in text.splitlines():
        if not line.startswith(FORBIDDEN_LINE_PREFIX):
            continue
        rest = line[len(FORBIDDEN_LINE_PREFIX):].strip()
        if not rest or rest.lower() == "none specified":
            return []
        names = []
        for item in rest.split(","):
            name = item.strip().removesuffix("()").strip()
            if name:
                names.append(name)
        return names
    return []


def used_forbidden_functions(source: str, forbidden: list[str]) -> list[str]:
    if not forbidden:
        return []
    bare = {name for name in forbidden if "." not in name}
    dotted = {name for name in forbidden if "." in name}

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    used: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Name) and func.id in bare:
            used.add(func.id)
        elif isinstance(func, ast.Attribute):
            if func.attr in bare:
                used.add(func.attr)
            if isinstance(func.value, ast.Name):
                qualified = f"{func.value.id}.{func.attr}"
                if qualified in dotted:
                    used.add(qualified)
    return sorted(used)
