#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
"""

class MyList(list):
    """Class inherits from list class"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
