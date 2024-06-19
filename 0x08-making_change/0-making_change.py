#!/usr/bin/python3
"""Module to datermine fewer coins to reach given account"""


def makeChange(coins, total):
    """Function to check the needed coins"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for c in coins:
        for r in range(c, total + 1):
            dp[r] = min(dp[r], dp[r - c] + 1)

    return dp[total] if dp[total] != float('inf') else -1
