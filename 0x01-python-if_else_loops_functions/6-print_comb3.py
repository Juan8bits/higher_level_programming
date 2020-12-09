#!/usr/bin/python3
for dec in range(0, 10):
    for uni in range(0, 10):
        if uni != dec and uni > dec:
            if uni > 1:
                print(', ', end='')
            print('{:d}{:d}'.format(dec, uni), end='')
print('\n')
