# Mad Libs
# Mad Libs program that reads in text files and lets the user add their own text 
# Promot User to replace the words ADJECTIVE, NOUN, ADVERB, or VERB
# The results should be printed to the screen and saved to a new text file

import re

with open("madlab.txt",'r',errors='ignore') as f:
    content = f.read()

# Regular expression for each searchable word
grammer_reg = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = grammer_reg.findall(content)

# For each match prompt the user for a replacement
for match in matches:
    replacement = input('Please enter a '+match+"\n")
    content = content.replace(match, replacement)
      
print(content)
with open("madlabComplete.txt",'w',errors='ignore') as f:
  f.write(content)