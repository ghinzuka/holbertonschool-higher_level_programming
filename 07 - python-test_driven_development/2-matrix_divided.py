#!/usr/bin/python3
""" function that divide a matrix by two a round at 2 after decimal
matrix: list of element
div: number to divide each element of the list
raise typeError if element are not float or int and matrix is not a list
raise typeError if the row in the matric are not the same size
raise a typeError if Div is not a float or an int and
raise dividebyzero if div is 0
return the result  with two decimal"""


def matrix_divided(matrix, div):

    """ function that divide a matrix by two a round at 2 after decimal
    return the result round at two decimal
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(error)

    ref_row = len(matrix[0])
    for i in matrix:
        if len(i) != ref_row:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(j / div, 2) for j in i] for i in matrix]
