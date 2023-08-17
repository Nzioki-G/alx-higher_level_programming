#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary


"""
a_dictionary = { 'language': "C", 'Number': 89,\
      'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
[print(f"{k}: {v}") for k, v in a_dictionary.items()]
print("--")
[print(f"{k}: {v}") for k, v in new_dict.items()]

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'language')
[print(f"{k}: {v}") for k, v in a_dictionary.items()]
print("--")
[print(f"{k}: {v}") for k, v in new_dict.items()]
"""
