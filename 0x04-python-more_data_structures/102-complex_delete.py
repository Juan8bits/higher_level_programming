#!/usr/bin/python3
def complex_delete(a_d, value):
    [a_d.pop(x) for x in dict(a_d) if value == dict(a_d).get(x)]
    return a_d
