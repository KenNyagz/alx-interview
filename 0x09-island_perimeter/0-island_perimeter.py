#!/usr/bin/python3
'''
Finding the area of an island in a grid
'''


def island_perimeter(grid):
    '''Calculating perimeter of an island in a grid '''
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check if top boundary is water or edge of grid
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check if bottom is water or grid edge
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # check left boundary
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
