#!/usr/bin/python3
"""function that appends a string at the end of a
   text file (UTF8) and returns the number of characters
   added.
"""


def append_write(filename="", text=""):
    """append_write function"""
    with open(filename, mode="a", encoding="utf-8") as _file:
        return _file.write(text)
