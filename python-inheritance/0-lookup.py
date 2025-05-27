#!/usr/bin/python3
"""
A a function that returns the list of available attributes 
and methods of an object.
"""


def lookup(obj):
    """
    looks for attributes and methods

    Args:
    obj: object class

    Returns:
    list of available attributes and methods of the object.
    """
    return dir(obj)
