#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            num = matrix[row][col]
            print("{}".format(num), end="")
            if col < len(matrix[0]) - 1:
                print(end=" ")
        print()


"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
"""
