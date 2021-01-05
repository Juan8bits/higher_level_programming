#!/usr/bin/python3
"""Module that create a class called Square"""


class Square:
    """Class to manipulate a square.
    """

    def __init__(self, size=None):
        """Initialized method class with a size value.

            Args:
                size (int): Size of defined square.
        """
        self.__size = size
