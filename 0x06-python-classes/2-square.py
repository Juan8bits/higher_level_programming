#!/usr/bin/python3
"""Module that create a square."""


class Square:
    """Class to manipulate a square.
    """
    def __init__(self, size=0):
        """Initialized method class with a size value.

        Args:
            size (int): Size of defined square.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
