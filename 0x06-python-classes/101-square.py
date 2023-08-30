#!/usr/bin/python3
"""complex Square"""


class Square:
    '''co-ordinated of a square override of toString'''

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

    def __str__(self):
        """returns a string format of this square on an axis"""
        str_instance = []
        x, y = self.__position[0], self.__position[1]
        if self.__size == 0:
            str_instance.append("")
        else:
            for _ in range(y):
                str_instance.append("")

            spaces = ' ' * x
            for _ in range(self.__size):
                str_instance.append(spaces + "#" * self.__size)

        return "\n".join(str_instance)


"""
my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
"""
