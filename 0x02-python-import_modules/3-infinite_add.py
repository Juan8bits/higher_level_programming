#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    """ Program that add all arguments given """
    summation = 0
    for args in argv[1::1]:
        summation += int(args)
    print('{}'.format(summation))
