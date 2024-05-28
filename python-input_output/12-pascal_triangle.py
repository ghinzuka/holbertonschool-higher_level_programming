#!/usr/bin/python3
"""function that returns the Pascal triangle of n"""


def pascal_triangle(n):
    """function that returns the Pascal triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(0, n - 1):
        row = [1]
        triangle.append(row)
    return triangle
