#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print("{}".format(matrix[row][col]), end="")
            if col < len(matrix[0]) - 1:
                print(end=" ")
        print()
