# Character Picture Grid
# Print out the grid horizontally column by column
"""
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Get len(grid[0]) 6 for the row length and len(grid) 9 for column length
# Use these numbers to perform a reverse/flipped loop for the desired pattern

def flip_grid(grid):
  for i in range(len(grid[0])):
    for j in range(len(grid)):
      print(grid[j][i],end='')
    print()

if __name__ == '__main__':
  flip_grid(grid)    