#!/usr/bin/python3
"""
Module to create function to return list of integer list
representing pascals triangle
"""


def pascal_triangle(n):
    """Funcion to return a list to represent the pascal trangle"""
    if n <= 0:
        return []
    tri = [[1]]

    for r in range(1, n):
        row = [1]
        p_row = tri[r - 1]
        for g in range(1, r):
            row.append(p_row[g - 1] + p_row[g])
        row.append(1)
        tri.append(row)

    return tri
