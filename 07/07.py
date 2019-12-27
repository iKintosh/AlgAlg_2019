import numpy as np


def read_input():
    edges = []
    num_edges = int(input())
    for i in range(num_edges):
        edges.append(list(map(int, input().split())))
    edges = np.array(edges)
    num_points = len(np.unique(edges))
    adj_matrix = np.zeros((num_points, num_points))
    adj_matrix[edges[:, 0], edges[:, 1]] = 1
    adj_matrix[edges[:, 1], edges[:, 0]] = 1
    return adj_matrix


def get_figure_size(adj_matr):
    for i in range(2, adj_matr.shape[0] + 1):
        if np.all(adj_matr[:i, :i].sum(axis=0) == 2):
            return i


def get_edge_coord(adj_matr, fig_size):
    x = 0
    y = 0
    r = 1
    edge_coords = [(x + r * np.cos(2 * np.pi * i / fig_size), y + r * np.sin(2 * np.pi * i / fig_size)) for i in
                   range(1, fig_size + 1)]
    return np.array(edge_coords)


def solve_(adj_matr, coords, fig_size):
    A = adj_matr[fig_size:, fig_size:].copy()
    np.fill_diagonal(A, 3)
    A[A == 1] = -1
    b_x = np.zeros(adj_matr.shape[0] - fig_size)
    b_y = np.zeros(adj_matr.shape[0] - fig_size)
    for i in range(fig_size):
        for k in range(fig_size, adj_matr.shape[0]):
            if adj_matr[k, i] or adj_matr[i, k]:
                b_x[k - fig_size] = coords[i][0]
                b_y[k - fig_size] = coords[i][1]
    x_points = np.linalg.solve(A, b_x)
    y_points = np.linalg.solve(A, b_y)
    return x_points, y_points


adj_matr = read_input()
fig_size = get_figure_size(adj_matr)
coord = get_edge_coord(adj_matr, fig_size)
sol = solve_(adj_matr, coord, fig_size)
coord = np.round(coord, 3)
sol = np.round(sol, 3)

for i in range(len(coord)):
    print(i, coord[i][0], coord[i][1])
for i in range(len(sol[0])):
    print(fig_size + i, sol[0][i], sol[1][i])
