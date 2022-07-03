#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_array in matrix:
        x = 0
        for i in sub_array:
            if x == 0:
                print("{:d}".format(i), end="")
            else:
                print("{:< 1d}".format(i), end="")
            x += 1
        print()
