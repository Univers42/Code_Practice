GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

COLORS = {
    "green": GREEN,
    "red": RED,
    "white": WHITE,
    "gray": GRAY,
    "yellow": YELLOW,
    "blue": BLUE,
    "reset": RESET,
}

PROMPT = "@samushell: "


def colored(text: str, color: str) -> str:
    return f"{COLORS[color]}{text}{COLORS['reset']}"


def bracket_option(label: str, description: str) -> str:
    return f"{colored(f'[{label}]', 'yellow')} {description}"


def underlined_header(text: str) -> str:
    padded = f"{text}{' ' * 10}"
    return f"{BLUE}{UNDERLINE}{padded}{RESET}"


EXERCISES_3_LEVELS: list[tuple[str, list[str]]] = [
    (
        "Level 1",
        [
            "anagram",
            "echo_validator",
            "mirror_matrix",
            "shadow_merge",
            "string_sculptor",
        ],
    ),
    (
        "Level 2",
        [
            "bracket_validator",
            "cryptic_sorter",
            "hidenp",
            "inter",
            "string_permutation_checker",
            "twist_sequence",
            "whisper_cipher",
        ],
    ),
    (
        "Level 3",
        [
            "number_base_converter",
            "pattern_tracker",
        ],
    ),
]

EXERCISES_4_LEVELS: list[tuple[str, list[str]]] = [
    (
        "Level 1",
        [
            "firefly_grid",
            "gears_match",
            "shared_ingredients",
        ],
    ),
    (
        "Level 2",
        [
            "merge_milk_routes",
            "tallest_sunflowers",
        ],
    ),
    (
        "Level 3",
        [
            "ribbon_cuts",
            "workshop_setup_order",
        ],
    ),
]

EXERCISES_3 = [name for _, names in EXERCISES_3_LEVELS for name in names]
EXERCISES_4 = [name for _, names in EXERCISES_4_LEVELS for name in names]

LEVELS_BY_RANK = {
    3: EXERCISES_3_LEVELS,
    4: EXERCISES_4_LEVELS,
}
