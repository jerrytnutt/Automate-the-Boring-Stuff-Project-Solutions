# Write a function that takes a string and does the same thing as the strip() string method
# If a second argument is included remove its characters from the string.

import re

def regex_strip(str,remove=None):
  newString = str
  if remove == None:
    pattern = re.compile(r'^\s+|\s+$')
  else:
    pattern = re.compile(remove)
  for match in pattern.findall(str):
    newString = newString.replace(match, '') 
  return newString
  

txt = "     ban ana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
print(regex_strip('  John man  '))
print(regex_strip('    this is    a test      '))

