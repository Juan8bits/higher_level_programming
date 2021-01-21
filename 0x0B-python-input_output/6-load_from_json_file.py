#!/usr/bin/python3
"""Function that creates an Object from a JSON file."""


def load_from_json_file(filename):
    """load_from_json_file function."""
    import json
    with open(filename, mode="r") as ffile:
        return json.load(ffile)
