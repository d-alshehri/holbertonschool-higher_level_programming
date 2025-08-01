#!/usr/bin/python3
"""
Module that defines a function to append a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
