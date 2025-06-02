#!/usr/bin/python3
"""
Defines a function to count the number of lines in a text file.
"""

def number_of_lines(filename=""):
    """
    Counts the number of lines in a text file.
    """
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
