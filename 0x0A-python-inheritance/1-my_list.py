#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """class Mylist."""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
