def twist_sequence_solution(arr: list[int], k: int) -> list[int]:
    if len(arr) != 0:
        k = k % len(arr)
    return arr[-k:] + arr[:-k]
