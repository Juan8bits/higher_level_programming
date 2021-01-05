#!/usr/bin/python3
class Square:
    """Class to manipulate a square.

    Attributes:
        area (obj): Method for calculate area from a square.
        size: Setter and getter.

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

    @property
    def size(self):
        """Method to return (getter) the value of private attribute.

        Returns:
            Value of size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Method to setter private attribute.

        Args:
            value (int): New size of square.
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
