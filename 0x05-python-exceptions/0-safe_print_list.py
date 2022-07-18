#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        if x > 0:
            for i in my_list:
                print(i, end="")
                num += 1
                if num == x:
                    break
            print()
        return num

    except IndexError:
        return num
