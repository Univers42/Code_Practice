from dataclasses import dataclass

GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"
YELLOW = "\033[93m"
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


def separator_line(width: int = 40) -> str:
    return colored("-" * width, "gray")


# --- Rank 02 exercise kinds ----------------------------------------------------
# A rank 02 assignment is turned in as one or more .c files. How the shell
# compiles and runs it depends on whether the student's file provides its own
# entry point:
#
#   PROGRAM  -> the .c file has its own main(). Compile it on its own and run
#               the resulting binary, feeding it argv / stdin and comparing its
#               output against the reference.
#   FUNCTION -> the .c file only defines a function (no main). Compile it
#               together with a tester main provided by the shell, which calls
#               the function and prints results to compare.
PROGRAM = "program"
FUNCTION = "function"


@dataclass(frozen=True)
class Exercise:
    name: str
    kind: str  # PROGRAM or FUNCTION


EXERCISES_02_LEVELS: list[tuple[str, list[Exercise]]] = [
    (
        "Level 1",
        [
            Exercise("first_word", PROGRAM),
            Exercise("fizzbuzz", PROGRAM),
            Exercise("ft_putstr", FUNCTION),
            Exercise("ft_strcpy", FUNCTION),
            Exercise("ft_strlen", FUNCTION),
            Exercise("ft_swap", FUNCTION),
            Exercise("repeat_alpha", PROGRAM),
            Exercise("rev_print", PROGRAM),
            Exercise("rot_13", PROGRAM),
            Exercise("rotone", PROGRAM),
            Exercise("search_and_replace", PROGRAM),
            Exercise("ulstr", PROGRAM),
        ],
    ),
    (
        "Level 2",
        [
            Exercise("alpha_mirror", PROGRAM),
            Exercise("camel_to_snake", PROGRAM),
            Exercise("do_op", PROGRAM),
            Exercise("ft_atoi", FUNCTION),
            Exercise("ft_strcmp", FUNCTION),
            Exercise("ft_strcspn", FUNCTION),
            Exercise("ft_strdup", FUNCTION),
            Exercise("ft_strpbrk", FUNCTION),
            Exercise("ft_strrev", FUNCTION),
            Exercise("ft_strspn", FUNCTION),
            Exercise("is_power_of_2", FUNCTION),
            Exercise("last_word", PROGRAM),
            Exercise("max", FUNCTION),
            Exercise("print_bits", FUNCTION),
            Exercise("reverse_bits", FUNCTION),
            Exercise("snake_to_camel", PROGRAM),
            Exercise("swap_bits", FUNCTION),
            Exercise("union", PROGRAM),
            Exercise("wdmatch", PROGRAM),
        ],
    ),
    (
        "Level 3",
        [
            Exercise("add_prime_sum", PROGRAM),
            Exercise("epur_str", PROGRAM),
            Exercise("expand_str", PROGRAM),
            Exercise("ft_atoi_base", FUNCTION),
            Exercise("ft_list_size", FUNCTION),
            Exercise("ft_range", FUNCTION),
            Exercise("ft_rrange", FUNCTION),
            Exercise("hidenp", PROGRAM),
            Exercise("lcm", FUNCTION),
            Exercise("paramsum", PROGRAM),
            Exercise("pgcd", PROGRAM),
            Exercise("print_hex", PROGRAM),
            Exercise("rstr_capitalizer", PROGRAM),
            Exercise("str_capitalizer", PROGRAM),
            Exercise("tab_mult", PROGRAM),
        ],
    ),
    (
        "Level 4",
        [
            Exercise("flood_fill", FUNCTION),
            Exercise("fprime", PROGRAM),
            Exercise("ft_itoa", FUNCTION),
            Exercise("ft_list_foreach", FUNCTION),
            Exercise("ft_list_remove_if", FUNCTION),
            Exercise("ft_split", FUNCTION),
            Exercise("rev_wstr", PROGRAM),
            Exercise("rostring", PROGRAM),
            Exercise("sort_int_tab", FUNCTION),
            Exercise("sort_list", FUNCTION),
        ],
    ),
]

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

EXERCISES_02_ALL: list[Exercise] = [
    exercise for _, exercises in EXERCISES_02_LEVELS for exercise in exercises
]
EXERCISES_02: list[str] = [exercise.name for exercise in EXERCISES_02_ALL]
EXERCISES_02_BY_NAME: dict[str, Exercise] = {
    exercise.name: exercise for exercise in EXERCISES_02_ALL
}

EXERCISES_3 = [name for _, names in EXERCISES_3_LEVELS for name in names]
EXERCISES_4 = [name for _, names in EXERCISES_4_LEVELS for name in names]

LEVELS_BY_RANK = {
    2: EXERCISES_02_LEVELS,
    3: EXERCISES_3_LEVELS,
    4: EXERCISES_4_LEVELS,
}
