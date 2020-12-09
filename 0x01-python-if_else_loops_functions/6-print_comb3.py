#!/usr/bin/python3
for num in range(0, 100):
    if num % 10 > num / 10:#Units > tens
        if num < 89 and num > 0:
            print('{:02d}, '.format(num), end='')
        elif num == 89:
            print('{:02d}'.format(num))
