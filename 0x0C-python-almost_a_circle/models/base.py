#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """ Base class of all other classes in this project.

        Attributes:

        Methods:
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor class."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation
           of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries is []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation
           of list_objs to a file.
        """
        list_convert = [list_.to_dictionary() for list_ in list_objs]
        json_list = cls.to_json_string(list_convert)
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as _file:
            _file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
           representation json_string.
        """
        if json_string in (None, []):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attributes
           already set.
        """
        if (cls.__name__ is "Rectangle"):
            dummy = cls(4, 4)
        elif (cls.__name__ is "Square"):
            dummy = cls(16)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances"""
        try:
            file_name = cls.__name__ + ".json"
            with open(file_name, "r") as _file:
                content = _file.read()
                turn_in_content = cls.from_json_string(content)
                return [cls.create(**i) for i in turn_in_content]
        except FileNotFoundError:
            return []
