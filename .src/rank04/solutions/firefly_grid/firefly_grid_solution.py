def firefly_grid_solution(
    fireflies: list[tuple[int, int]], size: int
) -> list[str]:
    grid = [["."] * size for _ in range(size)]
    for row, col in fireflies:
        if 0 <= row < size and 0 <= col < size:
            grid[row][col] = "*"
    return ["".join(row) for row in grid]
