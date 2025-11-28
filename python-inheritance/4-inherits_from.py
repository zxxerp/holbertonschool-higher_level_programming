#!/usr/bin/python3
"""Module 4-inherits_from:
Defines a function to check if an object's class inherits from a
specified class
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, otherwise False.

    Example:
    >>> inherits_from(True, int)
    True
    >>> inherits_from(True, bool)
    False
    >>> inherits_from([], object)
    True
    >>> inherits_from(3, object)
    True
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
