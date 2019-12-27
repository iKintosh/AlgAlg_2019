import numpy as np


def find_max_column_element(column, current_row):
    column = list(np.abs(column[current_row:]))
    max_row = column.index(max(column)) + current_row
    return max_row


def swap_row(matrix, row_i: int, row_j: int):
    row1 = np.copy(matrix[row_i])
    row2 = np.copy(matrix[row_j])
    matrix[row_i] = row2
    matrix[row_j] = row1
    return matrix


def combine_row(matrix, row_i: int, row_j: int, coef):
    matrix[row_j] += coef * matrix[row_i]
    return matrix


def gauss_elimination_method(matrix):
    matrix = np.array(matrix)
    rows_num, columns_num = matrix.shape
    current_row, current_col = 0, 0

    for i in range(columns_num):
        max_row = find_max_column_element(matrix[:, i], current_row)
        if np.abs(matrix[max_row, current_col]) < 1e-10:
            raise ValueError
        if max_row != current_row:
            matrix = swap_row(matrix, current_row, max_row)
        for j in range(current_row + 1, rows_num):
            coef = - matrix[j, current_col] / matrix[current_row, current_col]
            matrix = combine_row(matrix, current_row, j, coef)
        current_row += 1
        current_col += 1
    return matrix


def calc(matrix):
    try:
        matrix = gauss_elimination_method(matrix)
    except ValueError:
        return False
    return matrix


if __name__ == '__main__':
    edges = int(input())
    vertex = []
    for _ in range(edges):
        vertex.append(list(map(int, input().split())))
    r = np.max(vertex) + 1
    matrix = np.zeros((r, r))
    for v in vertex:
        matrix[v[0], v[1]] = np.random.randint(1, 1000)
    for _ in range(10):
        res = calc(matrix)
        if isinstance(res, bool):
            continue
        else:
            break
    if isinstance(res, bool):
        print('no')
    else:
        print('yes')
