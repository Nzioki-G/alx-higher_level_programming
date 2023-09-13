#!/usr/bin/python3
'''Log parsing'''


import sys
from time import sleep
import signal

'''
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
 <arg 1>        <arg 2>   <arg 3>                      <arg 4>       <arg 5>
'''


def prnt():
    '''prints file size and status codes count'''
    print(f"File size: {file_size}")

    for key, val in stat_codes.items():
        if val == 0:
            continue
        print(f"{key}: {val}")


def handler(signum, frame):
    '''overrride the default ctrl+C interrupt'''
    prnt()
    exit(1)


# get the ^C signal and handle it
signal.signal(signal.SIGINT, handler)

count = 10
file_size = 0
stat_codes = {200: 0, 301: 0, 400: 0, 401: 0,
              403: 0, 404: 0, 405: 0, 500: 0}

for line in sys.stdin:
    stat = int(line.split(' ')[-2])
    size = int(line.split(' ')[-1])

    stat_codes[stat] += 1
    file_size += size
    count -= 1
    if count == 0:
        prnt()
        count = 10

'''
reference: https://code-maven.com/catch-control-c-in-python
'''
