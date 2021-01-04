#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p_el = 0
    iterator = 0
    try:
        while (iterator < x):
            if type(my_list[iterator]) is int:
                print("{:d}".format(my_list[iterator]), end='')
                p_el += 1
            iterator += 1
        print()
    except ValueError:
        pass
    return p_el
