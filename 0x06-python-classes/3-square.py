#!/usr/bin/python3
"""A blueprint of a square"""


class Square:
    """
    class that defines a square, initializes it
    performs attribute type/value verification
    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates the area of the class

        Returns:
                int: area of square
        """
        return (self.__size ** 2)
