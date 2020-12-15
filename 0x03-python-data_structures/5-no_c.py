#!/usr/bin/python3
def no_c(my_string):
    modify_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            modify_string += char
    return modify_string
