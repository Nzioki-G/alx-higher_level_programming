#!/usr/bin/python3
"""A blueprint of a square"""


class Square:
    """class that defines a square, initializes it"""
    __size = 0

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ retrieves the private attr size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the attribute size to given value"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates the area of the class"""
        area = self.__size ** 2
        return (area)

    def __lt__(self, other):
        if self.__size ** 2 < other.__size ** 2:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__size ** 2 <= other.__size ** 2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__size ** 2 == other.__size ** 2:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__size ** 2 != other.__size ** 2:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__size ** 2 > other.__size ** 2:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__size ** 2 >= other.__size ** 2:
            return True
        else:
            return False
