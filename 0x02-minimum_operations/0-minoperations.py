#!/usr/bin/python3
"""Module to calculate oparations needed for exact chars in a file"""


def minOperations(n):
    """
    Function to calculate the least opeartions needed to result exactly
    as characters in file
    :param n: The target number of H chars
    """
    if n <= 1:
        return 0
    for opt in range(2, n+1):
        if n % opt == 0:
            return minOperations(int(n/opt)) + opt
