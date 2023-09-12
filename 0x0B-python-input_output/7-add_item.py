#!/usr/bin/python3
'''Load, add, save'''


import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

# fetch any data in file
my_list = load("add_item.json")

# append the args to fetched data
my_list += sys.argv[1:]

# save new list to file
save(my_list, "add_item.json")
