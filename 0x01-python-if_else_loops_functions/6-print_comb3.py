#!/usr/bin/python3
for tens in range(9):
    for ones in range(10):
        if tens < ones:
            number = tens * 10 + ones
            if number == 89:
                print("{:02d}".format(number))
                break
            print("{:02d}".format(number), end=", ")
