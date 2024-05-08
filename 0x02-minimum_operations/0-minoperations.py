#!/usr/bin/python3
"""Module to calculate oparations needed for exact chars in a file"""


def minOperations(n):
    """
    Function to calculate the least opeartions needed to result exactly
    as characters in file
    """
    opts = 0
    cur_chs = 1
    clipboard = 0

    while cur_chs < n:
        if cur_chs * 2 > n and clipboard != 0:
            opts += 1
            cur_chs += clipboard
        elif cur_chs * 2 <= n:
            opts += 2
            clipboard = cur_chs
            cur_chs *= 2
        else:
            return 0

    return opts
