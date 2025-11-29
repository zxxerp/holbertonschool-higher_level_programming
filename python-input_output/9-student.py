#!/usr/bin/python3
"""
This module defines a Student class.
It demonstrates how to create a class that can serialize itself to dictionary.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        # We access the special __dict__ attribute which holds
        # all the writable instance variables as a dictionary.
        return self.__dict__
