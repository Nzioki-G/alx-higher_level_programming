#!/usr/bin/python3
"""A blueprint of a square"""


class Square:
    """
    class that defines, initializes it and verifies
    its field's type/value
    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
