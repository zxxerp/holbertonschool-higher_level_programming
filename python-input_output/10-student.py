#!/usr/bin/python3
"""
This module defines a Student class with filtering capabilities.
It demonstrates how to selectively serialize object data to prevent exposure.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, represents only those attributes.

        Args:
            attrs (list): (Optional) The list of attributes to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        # Get all attributes first
        my_dict = self.__dict__

        # Check if 'attrs' is a valid list of strings
        # We need to verify two things:
        #   a. Is 'attrs' a list?
        #   b. Is every item inside 'attrs' a string?
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            # Create a filtered dictionary
            # We assume the user might ask for attributes that don't exist,
            # so we use .get() or check 'if key in my_dict'.
            return {k: my_dict[k] for k in attrs if k in my_dict}

        # If filter is invalid or None, return everything
        return my_dict
