# Table Printer
# Write a function named printTable that takes a list of lists of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
# Display the strings in a table with each column right-justified. 
"""
  apples Alice  dogs 
 oranges   Bob  cats 
cherries Carol moose 
  banana David goose
"""

def table_Print(table):
  # Collect list of length of longest string for each inner list
  colWidths = [0] * len(table)

  for i in range(len(table)):
    longestString = max(table[i], key = len) 
    colWidths[i] = len(longestString)


  # loop through the table column by column

  for x in range(len(table[0])):
    print() # print statement for spacing
    for y in range(len(table)):
      # Use the longest string and rjust function to give each string proper spacing
      print(table[y][x].rjust(colWidths[y]),end=' ')
      
table_Print(tableData)   