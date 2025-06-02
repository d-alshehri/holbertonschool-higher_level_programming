#!/usr/bin/python3
"""
Function that returns the dictionary description for
JSON serialization of an object.
"""


def class_to_json(obj):

    """
    Returns the dictionary representation of a simple data structure
    for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing all serializable attributes.
    """
    return obj.__dict__
