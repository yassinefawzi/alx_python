def square_matrix_simple(matrix=[]):
    out = [[0 for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            out[i][j] = matrix[i][j] ** 2
    return out