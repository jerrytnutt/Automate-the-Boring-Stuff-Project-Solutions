# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. 
# If number is even, collatz() prints and returns (number // 2) 
# If number is odd, then collatz() prints and returns (3 * number + 1)
# Use try and except to make sure the user inputs and int type string

def collatz(number):
    if number == 1:
        return number
    elif number % 2 == 0:
        number = (number//2)
    elif number % 2 == 1:
        number =  (3 * number) + 1
    print(number)
    return collatz(number)

while True:
  number = input('Enter a number: ')
  try:
    collatz(int(number))
    break
  except:
    print('Please enter an integer')




