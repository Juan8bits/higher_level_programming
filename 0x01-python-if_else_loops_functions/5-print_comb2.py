#!/usr/bin/python3
for num in range(0, 100):
    if num > 0:
        print(', ', end='')
    print('{:d}'.format(num) if num > 9 else '0{:d}'
          .format(num), end='')
print('\n')
