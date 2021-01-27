#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class to define Rectangle.

    Atributes:
        __width(int): Width of the rectangle (Private)
        __heigth(int): Height of the rectangle (Private)
        __x:
        __y:

    Methods:
        width: Public method setter and getter.
        height: Public method setter and getter.
        x: Public method setter and getter.
        y: Public method setter and getter.
        area: Return are of Rectangle object.
        display: Showed a representation of Rectangle by # character.
        update: update attributes of and object.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Method to return (getter) the value of private attribute.
        Returns:
            Value of width.
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
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Method to return (getter) the value of private attribute.
        Returns:
                Value of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Method to setter private attribute.
        Args:
            value : New value of x
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Method to return (getter) the value of private attribute.
        Returns:
                Value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Method to setter private attribute.
        Args:
            value : New value of y
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Method that returns the area value of the Rectangle instance.

        Returns:
            Area of the Rectangle object (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the Rectangle instance
           with the character #. (W * H)
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Informal representation of Rectangle"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method that
           assigns an argument to each attribute.

           1st argument should be the id attribute.
           2nd argument should be the width attribute.
           3rd argument should be the height attribute.
           4th argument should be the x attribute.
           5th argument should be the y attribute.
        """
        attr = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            super().__init__(args[0])
            for i, value in enumerate(args[1:], 1):
                setattr(self, attr[i], value)
        else:
            for key in kwargs.keys():
                if key in attr:
                    if key is "id":
                        super().__init__(kwargs.get(key))
                    else:
                        setattr(self, key, kwargs.get(key))

    def to_dictionary(self):
        """Public method that returns the dictionary representation
           of a Rectangle.
        """
        attr = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attr}
