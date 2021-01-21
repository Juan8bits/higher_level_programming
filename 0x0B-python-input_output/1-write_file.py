#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
   and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write_file function."""
    with open(filename, mode="w", encoding="utf-8") as _file:
        return _file.write(text)
