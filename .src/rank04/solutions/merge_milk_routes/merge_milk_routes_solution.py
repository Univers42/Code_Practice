def merge_milk_routes_solution(routes: list[list[int]]) -> list[int]:
    pointers = [0] * len(routes)
    total = sum(len(route) for route in routes)
    result: list[int] = []
    for _ in range(total):
        best_index = -1
        best_value = 0
        for index, route in enumerate(routes):
            if pointers[index] >= len(route):
                continue
            value = route[pointers[index]]
            if best_index == -1 or value < best_value:
                best_index = index
                best_value = value
        result.append(best_value)
        pointers[best_index] += 1
    return result
