def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col < 0:
                print("{:d} ".format(col), end="")
            else:
                print(" {:d} ".format(col), end="")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)