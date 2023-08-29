#!/usr/bin/python3
"""not-so-simple functioning Square"""


class Square:
    '''Square with method to print itself'''

    def __init__(self, size=0):
        '''initializes a square by size
        optional att: size'''
        self.size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter: retrieves the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter: sets/updates the private attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square to stdout with character #"""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()


"""
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
"""
