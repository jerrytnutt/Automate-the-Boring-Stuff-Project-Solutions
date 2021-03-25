# Date Detection
# Write a Regular Expression that takes dates in DD/MM/YYYY
# Create a function that checks if the dates are valid 
# Rules for Leap Year:
  # Leap years are every year evenly divisible by 4 
  # Except for years evenly divisible by 100 
  # Unless the year is also evenly divisible by 400. 

import pyperclip, re

def date_validation(date):
  pattern = re.compile(""" 
            ([0][0-9]|[3][0-1]|[0-2][0-9])\/     # Days range from 01 to 31 
                                          
            ([0][0-9]|[1][0-2])          # Months range from 01 to 12 
                                          
            \/((1|2)\d\d\d)          # Years range from 1000 to 2999
            """,re.VERBOSE)

  for match in pattern.findall(date):
    date = match[0]+"/"+match[1]+"/"+match[2]
    day = match[0]
    month = match[1]
    year = match[2]

    # April, June, September, and November will have 30 days

    if month in ['04','06','09','11'] and day == '31': 
      return "Invalid Date, The month of {} does not have 31 days".format(month)

    elif month == '02' and day == '29' and int(year) % 4 == 0:
      # Check for leap year rules
      if int(year) % 100 == 0 and int(year) % 400 == 0:
        return "{} is a valid date".format(date)
      elif int(year) % 100 == 0:
        return "Invalid Date, The year {} is divisible by 4 and 100".format(year)
      else:
        return "{} is a valid date".format(date)

    elif month == '02' and int(day) <= 28:
      return "{} is a valid date".format(date)
    else: # Normal date that passed regex
      return "{} is a valid date".format(date)
  if len(pattern.findall(date)) == 0:
    return "{} is an Invalid date".format(date)
 

if __name__ == "__main__":
  # Test cases
  print(date_validation('21/06/2061'))  # True
  print(date_validation('31/11/2019'))  # False: 31st of november
  print(date_validation('29/02/2004'))  # True:  29 days in leap year
  print(date_validation('29/02/2100'))  # False: leap year divisible by 100
  print(date_validation('29/02/2000'))  # True: leap years divisible by 100 and 400