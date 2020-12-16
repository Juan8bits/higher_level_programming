#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        aux = my_list[0]
        for num in my_list:
                if num > aux:
                    aux = num
        return aux
    return None
