#!/usr/bin/python3
"""N queens"""


import sys


def recursive_helper(n):
    '''place queen, check for collisions, backtrack repeat'''
    current_placement = [0] * n
    non_attacking(0, current_placement, n)


def non_attacking(current_row, col_placement, board_size):
    if current_row == board_size:
        '''we have a full board; print'''
        board = []
        for row, col in enumerate(col_placement):
            board.append([row, col])
        print(board)
        return

    for col in range(board_size):
        if is_placeable(current_row, col, col_placement):
            col_placement[current_row] = col
            non_attacking(current_row + 1, col_placement, board_size)
    return



def is_placeable(row, col, col_placement):
    # if col_placements = [2, 0, 3] the only option left is col 1
    """
        0   1   2   3
    0   _ | _ | Q | _
    1   Q | _ | _ | _
    2   _ | _ | _ | Q
    3   F |*T*| F | F
    """
    for i in range(row):
        # (0,1) ==> (i, col_at_row_i) (2,3) ==> (row, col_at_curr_row)
        # e.g (0,1) & (2,3)   abs(1 - 3) = 2           abs(0 - 2) = 2
        # same_diagonal: change_in_x / change_in_y == 1
        in_same_diagonal = abs(col_placement[i] - col) == abs(i - row)
        in_same_col = col_placement[i] == col
        if in_same_diagonal or in_same_col:
            return False
    return True


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
