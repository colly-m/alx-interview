#!/usr/bin/python3
"""Module to determine amount of less coins to reach a given account"""


def makeChange(coins, total):
    """Function to check the needed coins"""
    temp_val = 0
    coins.sort(reverse=True)

    if total <= 0:
        return 0

    for c in coins:
        if total % c <= total:
            temp_val += total // c
            total = total % c

    return temp_val if total == 0 else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
