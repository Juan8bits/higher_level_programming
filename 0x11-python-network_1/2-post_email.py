#!/usr/bin/python3
""" POST request that passed an email as a parameter
    and display de body response.
"""
from urllib import request, parse
from sys import argv

if __name__ == '__main__':

    data = parse.urlencode({'email': argv[2]})
    data = data.encode()
    # Construc the request
    req = request.Request(argv[1], data=data)
    # Go to the url with the request.
    with request.urlopen(req) as response:
        print(response.read().decode())
