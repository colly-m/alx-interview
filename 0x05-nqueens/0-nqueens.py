#!/usr/bin/python3
"""Module to solve the N queens problem"""
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_qn = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_qn < 4:
    print('N must be at least 4')
    exit(1)


def prob_nqueens(n):
    """Function to handle the nqueens"""
    if n == 0:
        return [[]]
    in_solution = prob_nqueens(n - 1)
    return [sol + [(n, i + 1)]
            for i in range(n_qn)
            for sol in in_solution
            if ok_queen((n, i + 1), sol)]


def offence_queen(square, queen):
    """Function to have the queen on attack mode"""
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def ok_queen(sq, queens):
    """Function to check if queen is safe on the board"""
    for queen in queens:
        if offence_queen(sq, queen):
            return False
    return True


for answer in reversed(prob_nqueens(n_qn)):
    outcome = []
    for q in [list(q) for q in answer]:
        outcome.append([i - 1 for i in q])
    print(outcome)
