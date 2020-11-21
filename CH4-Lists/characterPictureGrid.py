# Character Picture Grid
# Print out the grid pattern horizontally column by column
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

# grab len(grid[0]) 6 for the row length and len(grid) 9 for column length
# Use these numbers to perform a reverse/flipped loop for the correct pattern

for i in range(len(grid[0])):
  if i != 0:
    print()
  for j in range(len(grid)):
    print(grid[j][i],end='')


    