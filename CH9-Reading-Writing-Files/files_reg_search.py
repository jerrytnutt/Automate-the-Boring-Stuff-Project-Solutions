# Write a program that opens all .txt files in a folder 
# Search for any line that matches a user-supplied regular expression
# The results should be printed to the screen

import re
import os
# Request the user for a regular expression input

regpat = input(r'enter reg expression: ')
pattern = re.compile(regpat)

#Search through all files in specified path that end in ".txt"
for f in os.listdir(r"PATH"):
    if f.endswith(".txt") == True:
        with open(f, "r", errors='ignore') as read_file:
            #Check text in file for any regex matches
            content = read_file.read()
            print(content)
            matches = pattern.finditer(content)
            for match in matches:
              print(match)
            





    