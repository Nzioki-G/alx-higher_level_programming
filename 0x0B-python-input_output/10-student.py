#!/usr/bin/python3
'''Student to JSON with filter'''


class Student:
    '''defines a student by __init__() & to_json() with filter'''

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


"""
student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
"""
