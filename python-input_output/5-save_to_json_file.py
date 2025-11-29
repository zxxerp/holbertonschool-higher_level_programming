#!/usr/bin/python3
"""
This module defines a function that writes a Python object to a file
using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file to write to.
    """
    # Open the file in write mode ('w') with UTF-8 encoding.
    # The 'with' statement ensures the file is closed automatically.
    with open(filename, mode="w", encoding="utf-8") as f:
        # json.dump() directly writes the object to the file stream.
        json.dump(my_obj, f)
