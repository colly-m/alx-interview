#!/usr/bin/python3
"""
Module to create function to return list of integer list
representing pascals triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    tri = [[1]]

    for r in range(1, n):
        row = [1]
        for g in range(1, r):
            if g < len(tri[r - 1]):
                row.append(tri[r - 1][g - 1] + tri[r - 1][g])

        row.append(1)
        tri.append(row)

    return tri
