#!/usr/bin/python3
"""Module to determine if a dataset is a valid UTF-8"""


def validUTF8(data):
    """Function to detemine if given data is valid utf8 encoding"""
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for n in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & n:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (n & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
