#!/usr/bin/python3
"""Fetches an URL and displays response body
"""
import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get(argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
