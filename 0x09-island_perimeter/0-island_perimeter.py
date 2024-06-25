#!/usr/bin/python3
"""Module to get perimeter of an island"""


def island_perimeter(grid):
    """Function tp return the perimeter"""
    perimeter = 0

    rows = len(grid)
    clm = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(clm):

            if grid[i][j] == 1:

                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
