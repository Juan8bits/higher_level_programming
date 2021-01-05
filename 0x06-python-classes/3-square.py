#!/usr/bin/python3
"""Module that create a class square"""


class Square:
    """Class to manipulate a square.

    Attributes:
        area (obj): Method for calculate area from a square.
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

    def area(self):
        """Method for calculate area from a square.

        This method call a private attribute sef.__size

        Returns:
            Area from a square.
        """

        return (self.__size ** 2)
