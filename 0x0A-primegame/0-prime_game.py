#!/usr/bin/python3
"""Module to solve a prime numbers in a game theory scenario"""


def sieve(n):
    """Generates prime status for numbers 0 to n from a list boolean"""
    is_p = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_p[p]:
            for i in range(p * p, n + 1, p):
                is_p[i] = False
        p += 1
    is_p[0], is_p[1] = False, False
    return is_p


def count_prime_num(is_p, n):
    """Count the number of primes up to and including n"""
    return sum(is_p[:n+1])


def isWinner(x, nums):
    """Function to checks for a player with most wins"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    is_p = sieve(max_num)

    maria_w = 0
    ben_w = 0

    for n in nums:
        num_primes = count_prime_num(is_p, n)

        if num_primes % 2 == 0:
            ben_w += 1
        else:
            maria_w += 1

    if maria_w > ben_w:
        return "Maria"
    elif ben_w > maria_w:
        return "Ben"
    else:
        return None
