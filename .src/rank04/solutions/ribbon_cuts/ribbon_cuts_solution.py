def ribbon_cuts_solution(ribbon: str) -> int:
    n = len(ribbon)
    if n == 0:
        return 0
    is_palindrome = [[False] * n for _ in range(n)]
    cuts = [0] * n
    for end in range(n):
        min_cuts = end
        for start in range(end + 1):
            same_ends = ribbon[start] == ribbon[end]
            short_span = end - start < 2
            inner_ok = short_span or is_palindrome[start + 1][end - 1]
            if same_ends and inner_ok:
                is_palindrome[start][end] = True
                if start == 0:
                    min_cuts = 0
                else:
                    min_cuts = min(min_cuts, cuts[start - 1] + 1)
        cuts[end] = min_cuts
    return cuts[n - 1]
