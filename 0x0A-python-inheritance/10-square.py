#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size):
        """Constructor class"""
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to calculate area"""
        return self.__size ** 2
