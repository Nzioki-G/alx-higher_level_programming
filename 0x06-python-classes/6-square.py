#!/usr/bin/python3
"""A blueprint of a square"""


class Square:
    """
    class that defines a square, initializes it
    performs attribute type/value verification
    """
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__position = position
        if (type(position) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) != int or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ():
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """ retrieves the private attr size
        Returns:
                the size atribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the attribute size to given value
            Args:
                @value(int/float): the value user provides
            Returns:
                    nothing
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """gets the attribute position
            Returns: the tuple position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the attribute position
            Args:
                @value(tupel): the tuple user enters
            Return: nothing
        """
        self.__position = value
        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ():
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates the area of the class
        Returns:
                int: area of square
        """
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """prints a square with #'s and spaces for position
            Returns: nothing
        """

        if self.__position[1] > 0:
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

        if self.__size == 0:
            print()
