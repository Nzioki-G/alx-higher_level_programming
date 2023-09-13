#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    '''returns the pascal triangle of n'''
    if n <= 0:
        return []
    return pascal_triangle_recursive(1, n, [], [])


def pascal_triangle_recursive(n, goal, prev, pascal):
    '''returns list of ints representing the
    Pascal's triangle of n'''
    array = [1] * n

    if n > 2:
        for idx in range(1, n // 2):
            val = prev[idx - 1] + prev[idx]
            array[idx] = val
            array[-idx - 1] = val
        if n % 2 == 1:
            mid = n // 2
            array[mid] = prev[mid - 1] + prev[mid]
    pascal.append(array)

    if n < goal:
        pascal_triangle_recursive(n+1, goal, array, pascal)
    return pascal


"""
def print_triangle(triangle):
    '''print the triangle'''
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(10))
"""
