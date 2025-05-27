#!/usr/bin/python3
"""
A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object's class is a subclass of the specified class,
    but not the specified class itself.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
