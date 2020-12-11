#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    leng = len(argv) - 1
    if leng == 0:
        print('0 arguments.')
    else:
        i = 1
        print('{} {}'.format(leng, 'argument:' if leng == 1 else 'arguments:'))
        for args in argv[1::1]:
            print('{}: {}'.format(i, args))
            i += 1
