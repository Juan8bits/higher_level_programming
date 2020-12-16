#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ Function that add new element in list """
    new = []
    for position in range(len(my_list)):
        if position == idx:
            new.append(element)
        else:
            new.append(my_list[position])
    return new

# Other way
#
# def new_in_list(my_list, idx, element):
#    new_list = my_list[:]
#    if idx in range(len(my_list)):
#       new_list[idx] = element
#       return new_list
#    return my_list
