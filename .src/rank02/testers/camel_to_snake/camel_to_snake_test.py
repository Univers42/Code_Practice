from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["hereIsACamelCaseWord"],
    ["helloWorld"],
    [""],
    ["a", "b"],
    [],
    ["alreadylower"],
    ["oneWord"],
    ["thisHasManyManyWords"],
    ["camelCase2Number"],
    ["x"],
]
