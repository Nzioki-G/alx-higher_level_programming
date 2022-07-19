#!/usr/bin/python3
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

    def area(self):
        """calculates the area of the class

        Returns:
                int: area of square
        """
        area = self.__size ** 2
        return (area)
