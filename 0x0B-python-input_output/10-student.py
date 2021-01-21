#!/usr/bin/python3
"""Class student."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Constructor method.

        first_name(str): string with the first_name of the student.
        last_name(str): string with the last_name of the student.
        age(int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method def to_json(self): that retrieves a
           dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for atributes in attrs:
            if atributes in self.__dict__:
                dic[atributes] = self.__dict__[atributes]
        return dic
