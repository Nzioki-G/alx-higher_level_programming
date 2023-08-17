#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


"""
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
[print(f"{k}: {v}") for k, v in new_dict.items()]
print("--")
[print(f"{k}: {v}") for k, v in a_dictionary.items()]

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
[print(f"{k}: {v}") for k, v in new_dict.items()]
print("--")
[print(f"{k}: {v}") for k, v in a_dictionary.items()]
"""
