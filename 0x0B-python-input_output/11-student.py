#!/usr/bin/python3
'''Student to disk and reload'''


class Student:
    '''Student by to_json() and reload_from_jsno() with filter'''

    def __init__(self, first_name, last_name, age):
        '''inits a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dict representation this instance
           if attributes are given, retrieve this instance's dict
           with only those specified attribues and their values
        '''
        if isinstance(attrs, list):
            att_dict = {}
            for string in attrs:
                try:
                    att = self.__getattribute__(string)
                    att_dict[string] = att
                except AttributeError:
                    pass
            return att_dict
        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of this instance
         @attr: json - a dict'''
        for key, val in json.items():
            try:
                self.__setattr__(key, val)
            except AttributeError:
                pass


'''
import os
import sys

read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name,
                        student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name,
                        new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name,
                        new_student_1.last_name, new_student_1.age))
'''
