#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    import numpy as np
    new_matrix = []

    # return, inner loop, outer loop
    new_matrix = [[np.power(col, 2) for col in row] for row in matrix]
    return new_matrix
