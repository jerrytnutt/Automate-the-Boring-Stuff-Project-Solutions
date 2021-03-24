# bulletPointAdder.py
# Add Wikipedia style bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
      # Adds proper style to lines 
      lines[i] = '* ' + lines[i]
     
text = '\n'.join(lines)
pyperclip.copy(text)

# Example Text
"""
Lists of animals
Lists of aquarium life
List of biologists by author abbreviation
"""
# Output
"""
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
"""
