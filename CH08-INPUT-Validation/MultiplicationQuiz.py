# Prompt user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
# If the user enters correct answer, display “Correct!” for 1 second.
# The user gets three tries to enter the correct answer.
# Eight seconds after first displaying the question, the question is marked as incorrect.

import pyinputplus as pyip
import random, time

correct_answers = 0

for i in range(10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = num1 * num2
    
    attempts = 0
    timeout = time.time() + 8
    while attempts < 3:
      answer = pyip.inputNum('{} x {} = '.format(num1,num2))
      if time.time() >= timeout:
          break
      if answer == num3:
        print('Correct!')
        correct_answers += 1
        time.sleep(1)
        break
      else:
        attempts += 1
print("Your score is {}%".format(correct_answers * 10))
