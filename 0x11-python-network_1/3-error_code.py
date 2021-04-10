#!/usr/bin/python3
""" Send a basic request to display the body but manage
    exceptions errors.
"""
from urllib import request, error
from sys import argv

if __name__ == '__main__':

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except error.HTTPError as _error:
        print("Error code: {}".format(_error.code))
