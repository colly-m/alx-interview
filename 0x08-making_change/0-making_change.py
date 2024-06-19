#!/usr/bin/python3
"""Module to datermine fewer coins to reach given account"""


def makeChange(coins, total):
    """Function to check the needed coins"""
    if total <= 0:
        return 0

    dop = [float('inf')] * (total + 1)
    dop[0] = 0

    for c in coins:
        for r in range(c, total + 1):
            dop[r] = min(dop[r], dop[r - c] + 1)

    return dop[total] if dop[total] != float('inf') else -1
