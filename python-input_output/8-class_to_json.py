#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    # All writable instance attributes are stored in the __dict__ attribute.
    # We simply return this dictionary.
    return obj.__dict__
