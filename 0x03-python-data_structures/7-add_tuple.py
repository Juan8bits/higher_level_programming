#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = list(tuple_a)
    tup_b = list(tuple_b)
    while len(tup_a) < 2:
        tup_a.append(0)
    while len(tup_b) < 2:
        tup_b.append(0)
    return (tup_a[0] + tup_b[0], tup_a[1] + tup_b[1])
