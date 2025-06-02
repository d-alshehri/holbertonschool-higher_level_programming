#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
and saves them to a file in JSON format.
"""

import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list from file if it exists, else start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
