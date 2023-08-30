#!/usr/bin/python3
"""kinda complex Square"""


class Square:
    '''coordinates of a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''initializes a square by size and position
        optional att: size, coordinates'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets/updates the position of a square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0 or value[0] != int or value[1] != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square to stdout with character # on axis"""
        x, y = self.__position[0], self.__position[1]
        if self.__size == 0:
            print()
        else:
            for _ in range(y):
                print()

            spaces = ' ' * x
            for _ in range(self.__size):
                print(spaces, end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()


"""
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (1, "3"))
my_square_3.my_print()

print("--")
"""
