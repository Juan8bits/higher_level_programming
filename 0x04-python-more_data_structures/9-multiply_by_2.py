#!/usr/bin/python3
def multiply_by_2(a_d):
    return dict(zip(a_d, map(lambda v: v*2, a_d.values())))
