#!/usr/bin/python3
"""Create a function that returns a list of lists
   of integers representing the Pascals triangle of n.
"""


def pascal_triangle(n):
    """Pascal_triangle function"""
    if n <= 0:
        return []
    trow = [1]
    pascal = []
    y = [0]
    for x in range(n):
        pascal.append(trow)
        trow = [left + right for left, right in zip(trow + y, y + trow)]
    return pascal
