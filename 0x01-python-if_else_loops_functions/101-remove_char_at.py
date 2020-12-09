#!/usr/bin/python3
def remove_char_at(str, n):
    string = ''
    i = 0
    for char in str:
        if i != n:
            string += char
        i += 1
    return string
