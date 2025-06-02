#!/usr/bin/python3


"""
Module that defines a function to convert a JSON string to a Python object.
"""


import json


def from_json_string(my_str):

    
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)
