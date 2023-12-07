def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col < 0:
                print("{:d} ".format(col), end="")
            else:
                print(" {:d} ".format(col), end="")
        print()