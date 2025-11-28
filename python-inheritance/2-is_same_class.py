#!/usr/bin/python3
"""Module 2-is_same_class: defines a function to check exact class of an object"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False.

    Example:
    >>> is_same_class(1, int)
    True
    >>> is_same_class(True, int)
    False
    >>> is_same_class("hello", str)
    True
    >>> is_same_class([], list)
    True
    """
    return type(obj) is a_class
