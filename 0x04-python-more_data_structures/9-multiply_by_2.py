#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * v
    return new_dict


"""
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
[print(f"{k}: {v}") for k, v in sorted(a_dictionary.items())]
print("--")
[print(f"{k}: {v}") for k, v in sorted(new_dict.items())]
"""
