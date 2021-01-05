#!/usr/bin/python3
"""Module that create a class called square."""


class Square:
    """Class to manipulate a square.

    Attributes:
        area: Method for calculate area from a square.
        size: Setter and getter.
        my_print: Method for print square.
    """

    def __init__(self, size=0):
        """Initialized method class with a size value.

        Fields:
            size (int): Size of defined square.
        Methods:
            __size (int): Privated method of field size.
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

    def my_print(self):
        """Method to print a square.
        """

        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end="")
                print()
