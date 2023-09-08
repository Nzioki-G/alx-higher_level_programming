#!/usr/bin/python3
'''Matrix multiplication'''


def matrix_mul(m_a, m_b):
    '''multiplies 2 matrices'''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # [1, 2]    *     [1, 2]    =    [7, 10]
    # [3, 4]          [3, 4]         [15, 22]
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]

    rows_a = len(m_a[0])
    rows_b = len(m_b[0])
    for ra in range(len(m_a)):
        if len(m_a[ra]) != rows_a:
            raise TypeError("each row of m_a must be of the same size")

        for col in range(len(m_b[0])):
            for row in range(len(m_b)):
                if len(m_b[row]) != rows_b:
                    raise TypeError("each row of m_b must be of the same size")
                
                elem_a = m_a[ra][row]
                elem_b = m_b[row][col]

            if not isinstance(elem_a, int) and not isinstance(elem_a, float):
                raise TypeError("m_a should contain only integers or floats")
            if not isinstance(elem_b, int) and not isinstance(elem_b, float):
                raise TypeError("m_b should contain only integers or floats")

            result[ra][col] += elem_a * elem_b

    return result


"""
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
"""
