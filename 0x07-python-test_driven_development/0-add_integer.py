#!/usr/bin/python3
"""Function to add two integers.
"""


def add_integer(a, b=98):
    """function that adds 2 integers.

    Return: Add a, b.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)
        return a + b
