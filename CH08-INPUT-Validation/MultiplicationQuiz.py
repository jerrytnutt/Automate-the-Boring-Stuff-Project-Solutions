# Prompt user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
# If the user enters correct answer, display “Correct!” for 1 second.
# The user gets three tries to enter the correct answer.
# Eight seconds after first displaying the question, the question is marked as incorrect.

import pyinputplus as pyip
import random, time

def start_quiz():
  correct_answers = 0
  for i in range(3):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = num1 * num2
    
    attempts = 0
    timeout = time.time() + 8
    while attempts < 3:
      answer = input('{} x {} = '.format(num1,num2))
      print(type(answer))
      try:
        int(answer)
        if time.time() >= timeout:
          break
        if int(answer) == num3:
          print('Correct!')
          correct_answers += 1
          time.sleep(1)
          break
        else:
          attempts += 1
      except:
        print('Please enter a number')
        attempts += 1
      
  return "Your score is {}%".format(correct_answers * 10)

if __name__ == "__main__":
  print(start_quiz())
