#!/usr/bin/python3
"""Module to rotate a matrix clockwise at 90"""


def rotate_2d_matrix(matrix):
    """Function to transpose the matrix"""
    n = len(matrix)

    for a in range(n):
        for e in range(a, n):
            matrix[a][e], matrix[e][a] = matrix[e][a], matrix[a][e]

    for a in range(n):
        matrix[a].reverse()
