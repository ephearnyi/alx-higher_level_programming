#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    one_matrix = matrix.copy()

    for i in range(len(matrix)):
        one_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    
    return (one_matrix)

