#!/usr/bin/python3
"""
This module defines a function to append text to a file.
It demonstrates file I/O operations using the 'a' mode for log preservation.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number
    of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    # open() with mode="a" appends to the end of the file.
    # If the file does not exist, it creates it.
    with open(filename, mode="a", encoding="utf-8") as f:
        # f.write() appends the text.
        # It returns the number of characters written.
        return f.write(text)
