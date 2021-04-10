#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    req = requests.post(url, data=data)
    try:
        json_answ = req.json()
        if json_answ:
            print("[{}] {}".format(json_answ['id'], json_answ['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
