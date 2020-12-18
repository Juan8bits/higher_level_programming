#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Function that replaces all occurrences
        of an element by another in a new list."""
    new_list = my_list[:]
    for position in range(len(my_list)):
        if my_list[position] == search:
            del new_list[position]
            new_list.insert(position, replace)
    return new_list
