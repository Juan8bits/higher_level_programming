#!/usr/bin/python3
def lookup(obj):
    """Function that return available attributes and methods
       of an object.
    """
    return list(dir(obj))
