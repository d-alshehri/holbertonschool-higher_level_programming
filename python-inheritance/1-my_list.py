#!/usr/bin/python3
"""
A class that inherits from list with a method to print the list sorted.
"""

class MyList(list):
    """MyList class that inherits from list and adds a method to print sorted list."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the list."""
        print(sorted(self))
