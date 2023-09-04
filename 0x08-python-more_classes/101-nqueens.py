#!/usr/bin/python3
"""N queens"""


import sys


def recursive_helper(n):
    '''place queen, check for collisions, backtrack repeat'''
    pass


'''place N none-attacking queens on an N x N chessboard'''
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
n = sys.argv[1]
try:
    n = int(n)
except ValueError:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
recursive_helper(n)
