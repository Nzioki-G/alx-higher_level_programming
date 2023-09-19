#!/usr/bin/python3
'''First Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''rectangle that inherits from base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructs using super (base)'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''gets the private attr width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets/updates the private attr width'''
        self._validate_is_int("width", value)
        self._validate_greater_than_zero("width", value)
        self.__width = value

    @property
    def height(self):
        '''gets the private attr height'''
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_is_int("height", value)
        self._validate_greater_than_zero("height", value)
        '''sets/updates the private attr height'''
        self.__height = value

    @property
    def x(self):
        '''gets the private attr x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets/updates the private attr x'''
        self._validate_is_int("x", value)
        self._validate_positive("x", value)
        self.__x = value

    @property
    def y(self):
        '''gets the private attr y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets/updates the private attr y'''
        self._validate_is_int("y", value)
        self._validate_positive("y", value)
        self.__y = value

    def _validate_is_int(self, attr_name, value):
        '''validates that an attribute is an integer'''
        if value.__class__.__name__ != int.__name__:
            raise TypeError(f"{attr_name} must be an integer")

    def _validate_greater_than_zero(self, attr_name, value):
        '''validates that an attr is greater than 0'''
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def _validate_positive(self, attr_name, value):
        '''validates that an attribute is >= 0'''
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        '''returns area of this instance'''
        return self.width * self.height

    def display(self):
        '''prints this instance with # characters'''
        rect = '\n' * self.y
        rect += (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rect[:-1])

    def __str__(self):
        '''returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return (f"[{__class__.__name__}] ({self.id}) \
{self.x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        '''updates this instance; assigns an arg to each attribute'''
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''returns the dict representation of a Rectangle'''
        attributes = ['id', 'width', 'height', 'x', 'y']
        my_dict = {}
        for attr in attributes:
            my_dict[attr] = self.__getattribute__(attr)
        return my_dict
