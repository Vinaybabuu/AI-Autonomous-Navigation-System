import random

def create_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.2:
                grid[i][j] = 1

    return grid