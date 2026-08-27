def mirror_matrix_solution(matrix: list[list[int]]) -> list[list[int]]:
    new_list: list[list[int]] = []
    for index in matrix:
        new_list.append(index[::-1])
    return new_list
