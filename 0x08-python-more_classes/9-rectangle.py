#!/usr/bin/python3
""" This module define a rectangle. """


class Rectangle:
    """Class to manipulate a rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle base
           on the area."""

        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle instance where
           width == height == size.
        """
        return Rectangle(size, size)

    def __del__(self):
        """Privated instance method to delete"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def __str__(self):
        """Informal representation of the object Rectangle."""

        if 0 in [self.__width, self.__height]:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + '\n') *
                    self.__height)

    def __repr__(self):
        """Formal representation of the object Rectange."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
