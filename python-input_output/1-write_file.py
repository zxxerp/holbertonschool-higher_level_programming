#!/usr/bin/python3
"""
This module defines a function to write text to a file.
It demonstrates file I/O operations using the 'w' mode.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    # open() with mode="w" creates the file or overwrites it.
    # encoding="utf-8" ensures standard text handling.
    with open(filename, mode="w", encoding="utf-8") as f:
        # f.write() puts the text into the file.
        # It returns the number of characters written.
        return f.write(text)
