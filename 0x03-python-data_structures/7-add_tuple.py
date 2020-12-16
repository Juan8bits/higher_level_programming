#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tpla_values = []
    cont1 = 0
    cont2 = 2
    for num in tuple_a:
        if cont1 > 1:
            break
        tpla_values.append(num)
        cont1 += 1

    for num in tuple_b:
        if cont2 > 3:
            break
        tpla_values.append(num)
        cont2 += 1
    while len(tpla_values) <= 3:
        tpla_values.append(0)
    return (tpla_values[0] + tpla_values[2], tpla_values[1] + tpla_values[3])
