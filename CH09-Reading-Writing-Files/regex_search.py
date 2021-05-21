# Regex Search
# Opens all .txt files in a folder and search for any line that matches a user-supplied regular expression
# The results should be printed to the screen
import re
import os

reg_pat = input(r'Enter Regular Expression: ')
pattern = re.compile(reg_pat)
current_path = os.getcwd()
  
# Search through all files in specified path that end in ".txt"
for f in os.listdir(current_path):
  file_path = current_path+"\\"+f
  print("File Path: {}".format(file_path))
  if f.endswith(".txt") == True:
    with open(file_path, "r", errors='ignore') as read_file:
     # Check text in file for any regex matches
      content = read_file.read()
      matches = pattern.finditer(content)
      for match in matches:
        print("Match: {}".format(match.group())) 