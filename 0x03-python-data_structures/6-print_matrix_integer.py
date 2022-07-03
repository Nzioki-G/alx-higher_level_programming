#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 1
    for sub_array in matrix:
        for i in sub_array:
            str = " " if (i != len(sub_array) * x) else ""
            print("{:d}".format(i), end=str)
        x += 1
        print()
