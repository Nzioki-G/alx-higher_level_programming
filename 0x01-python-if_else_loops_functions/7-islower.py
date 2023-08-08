#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc >= 97 and asc <= 122:
        return True
    return False


'''
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
'''
