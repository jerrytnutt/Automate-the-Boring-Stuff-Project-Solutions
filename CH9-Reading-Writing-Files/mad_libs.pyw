# 1. Create a Mad Libs program that reads in text files and lets the user add their own text 
# 2. Replace the word ADJECTIVE, NOUN, ADVERB, or VERB
# 3. The program would find these occurrences and prompt the user to replace them.
# 4. The results should be printed to the screen and saved to a new text file

import re
# Open text file and grab content
with open("madlab.txt",'r',errors='ignore') as f:
    content = f.read()

# Regular expression for each searchable word
grammerReg = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = grammerReg.findall(content)

# For each match prompt the user for a replacement
for match in matches:
    replacement = input('Please enter a '+match+"\n")
    content = content.replace(match, replacement)
      
#The results should be printed to the screen and saved to a new text file
print(content)
with open("madlab.txt",'w',errors='ignore') as f:
    f.write(content)