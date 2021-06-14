# Write a program to read in the contents of several text files and insert the contents into a spreadsheet. 
# For the first file, output the first line to column 1, row 1. The second line to to column 1, row 2, And so on.
# The next file will be written to column 2, the next file to column 3, And so on.

from openpyxl import Workbook
import os

def spread_to_text():
  workbook = Workbook()
  sheet = workbook.active

  path = "Path with text files"
  files = os.listdir(path)

  column = 0
  for items in files:
    file_path = path+"\\"+items
    # Open each text file in the path
    with open(file_path, 'r') as myfile:
      column += 1
      row = 0
      Lines = myfile.readlines()
      
      for line in Lines:
        # For each line in the text file write to new row
        line = line.replace('\n', '')
        print(line)
        row += 1
        sheet.cell(row=row, column=column).value = line
  workbook.save(filename="textFileToSpreadsheet.xlsx")
 
if __name__ == "__main__":
  spread_to_text()