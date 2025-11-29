#!/usr/bin/env python3
import pickle


class CustomObject:
    """
    A custom class that demonstrates how to pickle (serialize)
    and unpickle (deserialize) Python objects.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the object with name, age, and student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's details in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            # We must use Write Binary because pickle writes bytes, not text.
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            # In a real app, we might log this error.
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from a file.
        This is a @classmethod because we are creating a new object
        from the class blueprint, not using an existing one.

        Args:
            filename (str): The file to load from.

        Returns:
            CustomObject: The loaded instance, or None if failed.
        """
        try:
            # We must use 'rb' (Read Binary).
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            # If file is missing or data is corrupt, return None as requested.
            return None
