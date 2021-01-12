#!/usr/bin/python3
""" This module define a rectangle. """


class Rectangle:
    """Class to manipulate a rectangle.
    """

    def __init__(self, width=0, height=0):
        """ Initialized method class with height and width value.

        Fields:
            __width (int): width for defined rectangle.
            __height (int): Height for defined rectangle.
        Methods:
            width: Setter and getter the private field __width.
            heigth: Setter and getter the private field __height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to return (getter) the value of private attribute.

        Returns:
            Value of heigth.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method to setter private attribute.

        Args:
            value (int): New size of width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Method to return (getter) the value of private attribute.

        Returns:
            Value of heigth.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method to setter private attribute.

        Args:
            value (int): New size of Height
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Public instance method to calculate area of rectangle.

        Return:
            Rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """"Public instance method to calculate perimeter of rectangle.

        Return:
            Rectangle perimeter.
        """
        if 0 in [self.__width, self.__height]:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Informal representation of the object Rectangle."""

        if 0 in [self.__width, self.__height]:
            return ""
        else:
            return (('#' * self.__width + '\n') * self.__height)
