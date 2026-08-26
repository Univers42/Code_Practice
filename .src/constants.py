GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"
RESET = "\033[0m"

COLORS = {
    "green": GREEN,
    "red": RED,
    "white": WHITE,
    "gray": GRAY,
    "reset": RESET,
}

PROMPT = "@samushell: "


def colored(text: str, color: str) -> str:
    return f"{COLORS[color]}{text}{COLORS['reset']}"


EXERCISE_NAMES = [
    "firefly_grid",
    "gears_match",
    "merge_milk_routes",
    "ribbon_cuts",
    "shared_ingredients",
    "tallest_sunflowers",
    "workshop_setup_order",
]
