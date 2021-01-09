#!/usr/bin/python3
"""Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Function that divide all elements of a matrix.

    Return:
        New matrix with divided elements.
    """

    except1 = 'matrix must be a matrix (list of lists) of integers/floats'
    n_el1 = 0
    n_el2 = 0
    #matrix != list
    if type(matrix) is not list:    
        raise TypeError(except1)
    for rows in matrix:
        #elements of matrix are not type list
        if type(rows) is not list:
            raise TypeError(except1)
        res = list(map(lambda x:type(x) not in (int, float), rows))
        n_el2 = len(res)
        if n_el1 == 0:
            n_el1 = n_el2
        if n_el2 != n_el1:
            #Rows doesn´t have the same leng
            raise TypeError('Each row of the matrix must have the same size')
        for rev in res:
            #Elements in elements of matrix are not int or float
            if rev == True:
                raise TypeError(except1)
    # div == 0 or not float, int.
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
        
    new_ma = list(map(lambda row: list(map(lambda value: round(value / div, 2), row)), matrix))
    return new_ma
