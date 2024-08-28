#!/usr/bin/python3
"""Module to get perimeter of an island"""


def island_perimeter(grid):
    """Function to return the perimeter of island"""
    perimeter = 0

    rows = len(grid)
    clmn = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(clmn):

            if grid[r][c] == 1:

                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
