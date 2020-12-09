#!/usr/bin/python3
def uppercase(str):
    for char in str:
        _int = ord(char)
        if _int in range(97, 124):
            _int = _int - 32
        print('{:c}'.format(_int), end='')
    print("")
