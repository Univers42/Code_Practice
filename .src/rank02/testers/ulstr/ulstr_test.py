from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["Hello World"],
    [""],
    ["3:21 Ba  tOut  moUn ki Ka di KE m'en Ka fe fot"],
    ["ALLCAPS"],
    ["nocaps"],
    ["MiXeD cAsE 123"],
    [],
    ["a", "b"],
]
