#!/usr/bin/python3
"""
This module defines a Student class with serialization
and deserialization capabilities.
It demonstrates the full cycle of saving object state and reloading it.
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
        my_dict = self.__dict__

        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: my_dict[k] for k in attrs if k in my_dict}

        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        # We iterate through the dictionary key-value pairs.
        # setattr(object, name, value) sets the attribute on the object.
        for key, value in json.items():
            setattr(self, key, value)
