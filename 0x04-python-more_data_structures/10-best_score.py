#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    name = None
    if a_dictionary:
        for key, val in a_dictionary.items():
            if max_score is None or max_score < val:
                max_score = val
                name = key
    return name


"""
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
"""
