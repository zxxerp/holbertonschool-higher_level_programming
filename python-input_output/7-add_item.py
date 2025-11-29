#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and then saves them to a file.
It demonstrates persistence by loading old data,updating it and saving it back.
"""
import sys

# Using the special __import__ syntax because the filenames start with numbers.
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Try to load the existing list from the file
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist (first run), initialize an empty list
    my_list = []

# Add the command line arguments to the list.
# sys.argv[0] is the script name itself, so we skip it using [1:]
# .extend() adds all items from one list (args) to another (my_list)
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
