#!/usr/bin/python3
'''multiple 2 matrices'''


def lazy_matrix_mul(m_a, m_b):
    '''uses a module to do the multiplication'''
    import numpy as np

    num1 = np.array(m_a)
    num2 = np.array(m_b)

    return num1.dot(num2)


"""
print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
"""
