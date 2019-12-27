def trick(n, step, move):
    print(f'GATE {3 * n + step * 12 + move} AND {0 + step} {n + step}')
    print(f'GATE {3 * n + step * 12 + 1 + move} AND {n + step} {2 * n + step}')
    print(f'GATE {3 * n + step * 12 + 2 + move} OR {0 + step} {n + step}')
    print(f'GATE {3 * n + step * 12 + 3 + move} AND {0 + step} {2 * n + step}')

    print(f'GATE {3 * n + step * 12 + 4 + move} NOT {3 * n + step * 12 + move}')
    print(f'GATE {3 * n + step * 12 + 5 + move} OR {3 * n + step * 12 + move} {3 * n + step * 12 + 1 + move}')

    print(f'GATE {3 * n + step * 12 + 6 + move} AND {3 * n + step * 12 + 4 + move} {3 * n + step * 12 + 2 + move}')
    print(
        f'GATE {3 * n + step * 12 + 7 + move} OR {3 * n + step * 12 + 5 + move} {3 * n + step * 12 + 3 + move}')

    print(f'GATE {3 * n + step * 12 + 8 + move} AND {3 * n + step * 12 + 6 + move} {2 * n + step}')
    print(f'GATE {3 * n + step * 12 + 9 + move} OR {3 * n + step * 12 + 6 + move} {2 * n + step}')

    print(f'GATE {3 * n + step * 12 + 10 + move} NOT {3 * n + step * 12 + 8 + move}')

    print(
        f'GATE {3 * n + step * 12 + 11 + move} AND {3 * n + step * 12 + 10 + move} {3 * n + step * 12 + 9 + move}')

    if step == 0:
        print(f'GATE {3 * n + 12} AND {3 * n} {3 * n + 4}')
        print(f'OUTPUT {n + 1} {3 * n + 12}')

    if step == n - 1:
        print(f'OUTPUT {n} {3 * n + 12}')

    print(f'OUTPUT {n + 2 + step} {3 * n + step * 12 + 7 + move}')
    print(f'OUTPUT {0 + step} {3 * n + step * 12 + 11 + move}')


n = int(input())
for i in range(n):
    if i > 0:
        move = 1
    else:
        move = 0
    trick(n, i, move=move)
