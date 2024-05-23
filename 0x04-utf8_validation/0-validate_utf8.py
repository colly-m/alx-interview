#!/usr/bin/python3
"""Module to determine if a dataset is a valid UTF-8"""


def validUTF8(data):
    """Function to detemine if given data is valid utf8 encoding"""
    n_bytes = 0

    for n in data:
        mask = 1 << 7
        if not n_bytes:
            while mask & n:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if n >> 6 != 0b10:
                return False

        n_bytes = n_bytes - 1

    return n_bytes == 0
