# Debugging Coin Toss
# The program has several bugs in it
# Run through the program and fix the bugs that keep the program from working correctly

import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads

# Change comparison of toss from guess to index of guess in tuple
if toss == ('heads', 'tails').index(guess):
    print('You got it!')
else:
    print('Nope! Guess again!')
    # Add second while statement to check for proper input
    guess = input()
    while guess not in ('heads', 'tails'):
      print('Guess the coin toss! Enter heads or tails:')
      # Correct the spelling of "guesss"
      guess = input()
    if toss == ('heads', 'tails').index(guess):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')