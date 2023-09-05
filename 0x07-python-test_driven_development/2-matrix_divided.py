#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of @matrix by @div"""
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        matrix_error()

    for row in matrix:
        if not isinstance(row, list):
            matrix_error()
        row_len = len(matrix[0])
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                matrix_error()
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix


def matrix_error():
    """raises type_error on invalid matrix input"""
    raise TypeError("matrix must be a matrix (list of lists)\
                     of integers/floats")


"""
matrix = [
    [1, '2', 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
"""
