# Write a function that uses regular expressions to check password strength

# A strong password is defined as one that...
  # Is at least eight characters long
  # Contains both uppercase and lowercase characters
  # Has at least one digit 

import re

def passwordRequest(password):
  if len(password) >= 8:
    upperCase = re.compile("[A-Z]")
    lowerCase = re.compile("[a-z]")
    digitCase = re.compile("[0-9]")
    
    if upperCase.findall(password) == []:
      return "{} must contain at least one upper case letter.".format(password)
    if lowerCase.findall(password) == []:
      return "{} must contain at least one lower case letter.".format(password)
    if digitCase.findall(password) == []:
      return "{} must contain at least one digit.".format(password)
    return "{} is a strong password.".format(password)
  else:
    return "{} must be at least 8 characters long".format(password)

      
  

print(passwordRequest('ghtyrfy66')) # False
print(passwordRequest('aS1T77GT')) # True
print(passwordRequest('tH66yy')) # False
print(passwordRequest('abc!@#123ABC<>/.,{}\\|')) # True


  







