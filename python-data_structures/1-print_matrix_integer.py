def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if len(row) == len(row) - 1:
                print("{:d}".format(col), end="")
            else:
                print("{:d} ".format(col), end="")
        print()