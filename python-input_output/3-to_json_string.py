#!/usr/bin/python3
"""
This module defines a function that converts a Python object
into a JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON string representation of the object.
    """
    # json.dumps() takes an object and returns a JSON string.
    # It handles lists, dicts, strings, ints, and booleans automatically.
    return json.dumps(my_obj)
