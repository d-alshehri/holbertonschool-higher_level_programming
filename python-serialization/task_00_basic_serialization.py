#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    Args:
        data (dict): Dictionary to serialize.
        filename (str): Name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file to a Python dictionary.
    
    Args:
        filename (str): Name of the input JSON file.
    
    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
