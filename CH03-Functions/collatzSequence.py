# The Collatz Sequence
# Write a function named collatz with number parameter.
# If number is even, return (number // 2) 
# If number is odd, return (3 * number + 1)
# Use try and except for correct int input.

def collatz(number):
    if number == 1:
        return number
    elif number % 2 == 0:
        number = (number//2)
    elif number % 2 == 1:
        number = (3 * number) + 1
    print(number)
    return collatz(number)

if __name__ == '__main__':
  while True:
    number = input('Enter a integer: ')
    try:
      collatz(int(number))
      break
    except:
      print('Please enter an integer')




