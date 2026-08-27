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


EXERCISES_02_LEVELS: list[tuple[str, list[str]]] = [
    (
        "Level 1",
        [
            "first_word",
            "fizzbuzz",
            "ft_putstr",
            "ft_strcpy",
            "ft_strlen",
            "ft_swap",
            "repeat_alpha",
            "rev_print",
            "rot_13",
            "rotone",
            "search_and_replace",
            "ulstr",
        ],
    ),
    (
        "Level 2",
        [
            "alpha_mirror",
            "camel_to_snake",
            "do_op",
            "ft_atoi",
            "ft_strcmp",
            "ft_strcspn",
            "ft_strdup",
            "ft_strpbrk",
            "ft_strrev",
            "ft_strspn",
            "is_power_of_2",
            "last_word",
            "max",
            "print_bits",
            "reverse_bits",
            "snake_to_camel",
            "swap_bits",
            "union",
            "wdmatch",
        ],
    ),
    (
        "Level 3",
        [
            "add_prime_sum",
            "epur_str",
            "expand_str",
            "ft_atoi_base",
            "ft_list_size",
            "ft_range",
            "ft_rrange",
            "hidenp",
            "lcm",
            "paramsum",
            "pgcd",
            "print_hex",
            "rstr_capitalizer",
            "str_capitalizer",
            "tab_mult",
        ],
    ),
    (
        "Level 4",
        [
            "flood_fill",
            "fprime",
            "ft_itoa",
            "ft_list_foreach",
            "ft_list_remove_if",
            "ft_split",
            "rev_wstr",
            "rostring",
            "sort_int_tab",
            "sort_list",
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

EXERCISES_02 = [name for _, names in EXERCISES_02_LEVELS for name in names]
EXERCISES_3 = [name for _, names in EXERCISES_3_LEVELS for name in names]
EXERCISES_4 = [name for _, names in EXERCISES_4_LEVELS for name in names]

LEVELS_BY_RANK = {
    2: EXERCISES_02_LEVELS,
    3: EXERCISES_3_LEVELS,
    4: EXERCISES_4_LEVELS,
}
