#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Construct method"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method to calculate area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Informal representation of the object Rectangle."""
        return "[Rectangle] {}/{}".format(str(self.__width),
                                          str(self.__height))
