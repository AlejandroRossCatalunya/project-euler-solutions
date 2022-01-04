'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

grid = []
for row in range(21):
    grid.append([1] * 21)
for row in range(1, 21):
    for column in range(1, 21):
        grid[row][column] = grid[row - 1][column] + grid[row][column - 1]
print(grid[20][20])
