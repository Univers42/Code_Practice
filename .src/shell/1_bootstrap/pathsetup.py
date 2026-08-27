import sys
from pathlib import Path

_shell_root = Path(__file__).resolve().parent.parent
for _entry in sorted(_shell_root.rglob("*")):
    if _entry.is_dir() and not _entry.name.startswith((".", "__")):
        sys.path.insert(0, str(_entry))
