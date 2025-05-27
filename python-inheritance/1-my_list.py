#!/usr/bin/python3
"""
A class that inherits from list with a method to print the list sorted.
"""

class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the list."""
        print(sorted(self))
