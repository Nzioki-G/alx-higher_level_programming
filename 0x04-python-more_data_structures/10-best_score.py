#!/usr/bin/python3
def best_score(a_dictionary):
    max_k = None
    if a_dictionary:
        max_val = 0
        for k, v in a_dictionary.items():
            if v > max_val:
                max_val = v
                max_k = k

    return max_k
