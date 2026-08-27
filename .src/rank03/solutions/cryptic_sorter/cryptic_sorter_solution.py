def cryptic_sorter_solution(strings: list[str]) -> list[str]:
    def sort_key(s: str) -> tuple[int, str, int]:
        return (len(s), s.lower(), sum(c.lower() in "aeiou" for c in s))

    result = list(strings)
    for i in range(1, len(result)):
        current = result[i]
        current_key = sort_key(current)
        j = i - 1
        while j >= 0 and sort_key(result[j]) > current_key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result
