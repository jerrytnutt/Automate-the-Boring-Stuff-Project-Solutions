# Write a program that Flips a coin 100 times and create a list with the results
# Find out if a streak of six heads or six tails comes up in the results ("HHHHHH" or "TTTTTT")
# Loop this experiment 10,000 times and return the probability of a streak

import random
import re

total_runs = 0            
streak_score = 0

def coin_flips():
    global streak_score,total_runs

    # Return results into a single string for regular expressions
    results = ''
    for i in range(100):
      value = random.randint(0, 1)
      if value == 0:
        results += "H"
      elif value == 1:
        results += "T"
    match = re.findall(r'(HHHHHH|TTTTTT)', results)
    if len(match) > 0:
      streak_score = streak_score +  1
    total_runs = total_runs + 1
    return total_runs 

if __name__ == '__main__':
  for i in range(10000):
    coin_flips()
  print("The Chance of a streak is: {}%".format(round(streak_score/total_runs * 100)))