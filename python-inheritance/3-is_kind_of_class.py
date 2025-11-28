#!/usr/bin/python3
"""Module 3-is_kind_of_class:
Defines a function to check if an object is an instance of a class
or an instance of a subclass
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass.

    Example:
    >>> is_kind_of_class(1, int)
    True
    >>> is_kind_of_class(True, int)
    True
    >>> is_kind_of_class("hello", str)
    True
    >>> is_kind_of_class([], list)
    True
    >>> is_kind_of_class([], object)
    True
    """
    return isinstance(obj, a_class)
