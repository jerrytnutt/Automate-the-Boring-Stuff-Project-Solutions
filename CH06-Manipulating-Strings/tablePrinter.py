# TablePrinter.py
# Write a function that takes a list of lists of strings
# Then displays that list in a table with each column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
# Output
"""
  apples Alice  dogs 
 oranges   Bob  cats 
cherries Carol moose 
  banana David goose
"""

def table_print(table):
  # Collect Length of longest string for each inner list
  col_widths = [0] * len(table)

  for i in range(len(table)):
    longest_string = max(table[i], key = len) 
    col_widths[i] = len(longest_string)
  # loop through the table column by column

  for x in range(len(table[0])):
    for y in range(len(table)):
      # Use the longest string and rjust function to give each string proper spacing
      print(table[y][x].rjust(col_widths[y]),end=' ')
    print()

if __name__ == '__main__':     
  table_print(tableData)   