#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last -= 10
if last > 5:
    str = "and is greater than 5"
elif last == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {last:d} {str}")
