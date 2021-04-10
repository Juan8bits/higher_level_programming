#!/usr/bin/python3
""" POST request that passed an email as a parameter
    and display de body response with the package requests.
"""
import requests
from sys import argv

if __name__ == '__main__':

    data = {'email': argv[2]}
    req = requests.post(argv[1], data=data)
    print(req.text)
