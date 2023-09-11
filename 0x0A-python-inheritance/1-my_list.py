#!/usr/bin/python3
'''My list'''


class MyList(list):
    '''inherits list'''

    def print_sorted(self):
        '''prints list sorted in asc'''
        new_list = self[:]
        new_list.sort()
        print(new_list)


"""
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
"""
