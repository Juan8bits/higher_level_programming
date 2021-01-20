#!/usr/bin/python3
"""101-add_attribute"""


def add_attribute(obj, name, value):
    """Function that add new attribute"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
