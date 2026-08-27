def cryptic_sorter_solution(strings: list[str]) -> list[str]:
    return sorted(
        strings,
        key=lambda s: (len(s), s.lower(), sum(c.lower() in "aeiou" for c in s))
    )
