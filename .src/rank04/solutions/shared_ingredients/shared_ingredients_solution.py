def shared_ingredients_solution(recipes: list[list[int]]) -> list[int]:
    if not recipes or any(len(recipe) == 0 for recipe in recipes):
        return []
    common = set(recipes[0])
    for recipe in recipes[1:]:
        common &= set(recipe)
    return sorted(common)
