#!/usr/bin/python3
"""Create a function that returns a list of lists
   of integers representing the Pascals triangle of n.
"""


def pascal_triangle(n):
    """Pascal_triangle function"""
    if n <= 0:
        return []
    pascal = [[1], [1, 1]]
    for i in range(1, n - 1):
        line = [1]
        for j in range(len(pascal[i]) - 1):
            line.extend([pascal[i][j] + pascal[i][j + 1]])
        line += [1]
        pascal.append(line)
    return pascal
