#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, val in enumerate(row):
            if i != len(row) - 1:
                print("{}".format(val), end=" ")
            else:
                print("{}".format(val), end="")
        print()
