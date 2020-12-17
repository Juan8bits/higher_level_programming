#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Function that computes the square
        value of all integers of a matrix."""

    copy = []
    for row in matrix:
        copy.append(list(map(square_from_number, row)))
    return (copy)


def square_from_number(n):
    """Function that return the square from a number."""

    return (n * n)
