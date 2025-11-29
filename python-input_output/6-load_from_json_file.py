#!/usr/bin/python3
"""
This module defines a function that creates an Object from a JSON file.
It demonstrates deserialization from a file stream.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        any: The Python object represented by the JSON file content.
    """
    # Open the file in read mode ('r') with UTF-8 encoding.
    # The 'with' statement ensures the file is closed automatically.
    with open(filename, mode="r", encoding="utf-8") as f:
        # json.load() reads the file and converts the JSON data
        # back into a Python object directly.
        return json.load(f)
