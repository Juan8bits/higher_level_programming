#!/usr/bin/python3
class Square:
    """Class to manipulate a square.

    Attributes:
        area: Method for calculate area from a square.
        size: Setter and getter.
        my_print: Method for print square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialized method class with a size value.

        Fields:
            size (int): Size of defined square.
            position (int tuple): Spaces before square.
        Methods:
            __size (int): Privated method of field size.
            __position (int tuple): Privated methods of field position.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
            self.__position = position

    @property
    def position(self):
        """Method to return (getter) the value of private attribute.

        Returns:
            Value of position.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Method to setter private attribute.

        Args:
            value (tuple): New size of separator.
        """
        if (type(value) != tuple or len(value) != 2 or
           type(value[0]) != int or
           type(value[1]) != int or
           value[0] < 0 or
           value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

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

    def area(self):
        """Method for calculate area from a square.

        This method call a private attribute sef.__size

        Returns:
             Area from a square.
        """

        return (self.__size ** 2)

    def my_print(self):
        """Method to print a square.
        """

        for spaces in range(self.__position[1]):
            print()
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(' ', end="")
                for i in range(self.__size):
                    print('#', end="")
                print()
