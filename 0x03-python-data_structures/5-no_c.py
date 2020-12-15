#!/usr/bin/python3
def no_c(my_string):
    modify_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            modify_string += char
            #print(modify_string)
    return modify_string
