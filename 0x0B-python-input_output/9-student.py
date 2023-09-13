#!/usr/bin/python3
'''Student to JSON'''


class Student:
    '''defines a student by __init__() & to_json()'''

    def __init__(self, first_name, last_name, age):
        '''inits a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dict representation this instance'''
        return self.__dict__


"""
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
"""
