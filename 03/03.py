import numpy as np


def read_input():
    matrix = []
    flag_while = True
    cnt = 0
    while flag_while:
        string = input().split()
        matrix_col = len(string) - 1
        if matrix_col == cnt:
            flag_while = False
        cnt += 1
        matrix.append(string)
    return np.array(matrix).astype(int)


def normalize(matrix):
    new_matrix = np.zeros((matrix.shape[0] + 1, matrix.shape[1] + 1))
    new_matrix[:-1, :-1] = matrix
    return new_matrix


def strassen_mul(A, B):
    if A.shape[0] == 1:
        return A * B

    if A.shape[0] % 2 != 0:
        A = normalize(A)
    if B.shape[0] % 2 != 0:
        B = normalize(B)
    if A.shape[0] != B.shape[0]:
        raise ValueError('A and B should have same shape')

    shape = int(A.shape[0] / 2)
    A_11, B_11 = A[:shape, :shape], B[:shape, :shape]
    A_12, B_12 = A[:shape, shape:], B[:shape, shape:]
    A_21, B_21 = A[shape:, :shape], B[shape:, :shape]
    A_22, B_22 = A[shape:, shape:], B[shape:, shape:]

    M_1 = strassen_mul((A_11 + A_22) % 9, (B_11 + B_22) % 9)
    M_2 = strassen_mul((A_21 + A_22) % 9, B_11 % 9)
    M_3 = strassen_mul(A_11 % 9, (B_12 - B_22) % 9)
    M_4 = strassen_mul(A_22 % 9, (B_21 - B_11) % 9)
    M_5 = strassen_mul((A_11 + A_12) % 9, B_22 % 9)
    M_6 = strassen_mul((A_21 - A_11) % 9, (B_11 + B_12) % 9)
    M_7 = strassen_mul((A_12 - A_22) % 9, (B_21 + B_22) % 9)

    C = np.zeros(A.shape)
    C[:shape, :shape] = (M_1 + M_4 - M_5 + M_7)[:shape, :shape]
    C[:shape, shape:] = (M_3 + M_5)[:shape, :shape]
    C[shape:, :shape] = (M_2 + M_4)[:shape, :shape]
    C[shape:, shape:] = (M_1 - M_2 + M_3 + M_6)[:shape, :shape]
    return C % 9


def power_matrix(matrix, power):
    current_power = 1
    power_dict = dict()
    power_dict[power] = None
    p = power
    while p != 1:
        if p % 2 == 0:
            power_dict[int(p / 2)] = None
            p = p / 2
        else:
            power_dict[int(p - 1)] = None
            p = p - 1
    power_dict[current_power] = matrix
    for i in sorted(power_dict.keys()):
        for j in sorted(power_dict.keys()):
            current_power = i + j
            if (current_power in power_dict) and (power_dict[current_power] is None) and (
                    power_dict[i] is not None) and (power_dict[j] is not None):
                power_dict[current_power] = strassen_mul(power_dict[i], power_dict[j])

    return power_dict


if __name__ == '__main__':
    matrix = read_input()
    power = shape = matrix.shape[0]
    answ = power_matrix(matrix, power)
    result = np.array(answ[power])[:shape, :shape].astype(int)
    string_result = ''
    for line in result:
        string_result += ' '.join(line.astype(str)) + '\n'
    print(string_result)
