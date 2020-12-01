# Write a program that Flips a coin 100 times and create a list with the results
# Find out if a streak of six heads or six tails comes up in the results "HHHHHH" or "TTTTTT"
# Loop this experiment 10,000 times and return the probability of a streak

import random
import re

totalRuns = 0            
streakScore = 0

def coinFips():
    global streakScore,totalRuns
    # Return results into a single string for regular expressions
    results = ''
    for i in range(100):
      value = random.randint(0, 1)
      if value == 0:
        results += "H"
      elif value == 1:
        results += "T"
    # Use regular expressions to check results sting
    match = re.findall(r'(HHHHHH|TTTTTT)', results)
    if len(match) > 0:
      streakScore = streakScore +  1
    totalRuns = totalRuns + 1

for i in range(10000):
  coinFips()

print("The Chance of a streak is: {}%".format(round(streakScore/totalRuns * 100)))