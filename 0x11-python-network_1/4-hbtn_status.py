#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status the msg method.
"""
from urllib import request

if __name__ == "__main__":

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print('Body response:')
        print('\t- type: {}'.format(type(response.msg)))
        print('\t- content: {}'.format(response.msg))
