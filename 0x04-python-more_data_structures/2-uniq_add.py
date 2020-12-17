#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Function that adds all unique integers in
        a list (only once for each integer).  """
    adds = 0
    for elements in set(my_list):
        adds += elements
    return adds
