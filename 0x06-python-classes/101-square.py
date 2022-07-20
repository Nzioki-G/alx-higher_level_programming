#!/usr/bin/python3
"""A blueprint of a square"""


class Square:
    """class that defines a square, initializes it"""
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """gets the attribute position"""
        return this.__position

    @position.setter
    def position(self, value):
        """sets the attribute position"""
        self.__position = value
        if ((type(value) != tuple) or (len(value) != 2) or
            (type(value[0]) != int or type(value[1]) != int) or
                (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates the area of the class"""
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """prints a square with #'s and spaces for position"""

        if self.__position[1] > 0:
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

        if self.__size == 0:
            print()

    def __str__(self):
        """prints similar to my_print()"""
        sq = []
        if self.__position[1] > 0:
            sq.append(str("\n"))

        for i in range(self.__size):
            sq.append(str(" ") * self.__position[0])
            sq.append(str("#") * self.__size)
            if i < self.__size - 1:
                sq.append("\n")
        if self.__size == 0:
            sq.append("\n")
        return "".join(sq)
