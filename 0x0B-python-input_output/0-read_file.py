#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read_file function"""
    with open(filename, mode="r", encoding="utf-8")as myfile:
        print(myfile.read(), end='')
