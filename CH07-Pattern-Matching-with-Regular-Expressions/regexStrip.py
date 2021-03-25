# Regex Version of the strip() Method
# Write a function that takes a string and performs the same thing as the strip() string method
# If a second argument is included remove its characters from the string

import re

def regex_strip(string,remove=None):
  if remove == None:
    pattern = re.compile(r'[^'+" "+'].*[^'+" "+']')
    new_string = pattern.search(string)
    return new_string.group()
  else:
    pattern = re.compile(remove)
  for match in pattern.findall(string):
    new_string = string.replace(match, '') 
  return new_string
  

if __name__ == "__main__":
  print(regex_strip('  Test 1'))
  print(regex_strip('  Test 2   '))
  print(regex_strip('Test 3   '))
  print(regex_strip('Test 5','T'))