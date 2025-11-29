#!/usr/bin/python3
"""
This module defines a function to read and print a text file.
It handles file I/O using the 'with' statement for resource safety.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to empty string.
    """
    # We use the 'with' statement to ensure the file is properly closed
    # automatically after the block is executed.
    # 'encoding="utf-8"' ensures we interpret special characters correctly.
    with open(filename, encoding="utf-8") as f:
        # f.read() reads the entire content into a string.
        # print() outputs it to stdout.
        # end="" prevents adding an extra newline, as the file content
        # usually already ends with one.
        print(f.read(), end="")
