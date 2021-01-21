#!/usr/bin/python3
"""Function that writes an Object to a text
   file, using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    import json
    with open(filename, mode="w") as _file:
        _file.write(json.dumps(my_obj))
