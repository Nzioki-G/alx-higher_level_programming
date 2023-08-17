#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    if my_list:
        total_score = 0
        total_weight = 0
        for score, weight in my_list:
            total_score += (score * weight)
            total_weight += weight
        average = total_score / total_weight
    return average


"""
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
"""
