#!/usr/bin/python3
'''And now, the Square!'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''inherits the behavior and validation of super'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''retrieves the size'''
        return self.width

    @size.setter
    def size(self, value):
        '''sets/updates the size of this square'''
        self.width = value
        self.height = value

    def __str__(self):
        '''overload to return square-like string'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        '''Updates the class Square; assigns attributes'''
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        '''return the dict rep of this instance'''
        my_dict = {}
        attributes = ['id', 'size', 'x', 'y']
        for attr in attributes:
            my_dict[attr] = self.__getattribute__(attr)
        return my_dict
