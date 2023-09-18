#!/usr/bin/python3
'''Base class'''
import json


class Base:
    '''the base of all other classes in this project'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor'''
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the json str rep of a list of dictsionaries'''
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the json str rep of a list of objects to file'''
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        try:
            with open(f"{cls.__name__}.json", "w") as my_file:
                data = cls.to_json_string(list_dicts)
                my_file.write(data)
        except FileNotFoundError:
            pass

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of dictionaries rep as json_string'''
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all atributes set'''
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        dicts = {}
        list_objs = []
        try:
            with open(f"{cls.__name__}.json", 'r') as my_file:
                data = my_file.read()
                dicts = cls.from_json_string(data)
        except FileNotFoundError:
            pass
        for dict in dicts:
            list_objs.append(cls.create(**dict))
        return list_objs
