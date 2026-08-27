from collections import deque


def tallest_sunflowers_solution(heights: list[int], k: int) -> list[int]:
    n = len(heights)
    if n == 0 or k <= 0 or k > n:
        return []
    window: deque[int] = deque()
    result: list[int] = []
    for index, value in enumerate(heights):
        while window and heights[window[-1]] <= value:
            window.pop()
        window.append(index)
        if window[0] <= index - k:
            window.popleft()
        if index >= k - 1:
            result.append(heights[window[0]])
    return result
