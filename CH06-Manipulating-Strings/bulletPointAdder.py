# Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
      # Removes any whitespace and adds proper casing 
      lines[i] = lines[i].lower().strip()
      lines[i] = '* ' + lines[i][0].upper()+lines[i][1:]
     
text = '\n'.join(lines)
pyperclip.copy(text)

# Example Text
"""
Lists of animals
lists of aquarium life
 lists of biologists by author abbreviation
"""
# Output
"""
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
"""
