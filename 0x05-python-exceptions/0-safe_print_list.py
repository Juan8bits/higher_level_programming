#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p_el = 0
    try:
        while (p_el < x):
            print(my_list[p_el], end='')
            p_el += 1
        print()
        return p_el
    except IndexError:
        print()
        return p_el
