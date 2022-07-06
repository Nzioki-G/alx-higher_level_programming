#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # EXOR gets elements present in EITHER not both
    return set(set_1) ^ set(set_2)
