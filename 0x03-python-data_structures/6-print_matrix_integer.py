#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            separador = ''
            for j in range(len(matrix[i])):
                print('{}{}'.format(separador, matrix[i][j]), end='')
                separador = ' '
            print()
