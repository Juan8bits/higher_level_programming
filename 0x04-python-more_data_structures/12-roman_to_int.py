#!/usr/bin/python3
def roman_to_int(rom_str):
    eq = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if rom_str and isinstance(rom_str, str):
        sum_ = 0
        for rn in range(len(rom_str)):
            if rom_str[rn] in eq.keys():
                current = eq.get(rom_str[rn])
                if rn > 0:
                    prev = eq.get(rom_str[rn - 1])
                    if prev >= current:
                        sum_ += current
                    else:
                        sum_ += current - (prev * 2)
                else:
                    sum_ += current
            else:
                return 0
        return sum_
    return 0
