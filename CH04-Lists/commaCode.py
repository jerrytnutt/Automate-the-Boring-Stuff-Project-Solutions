# Comma Code
# A function that takes a list and returns a string with all items separated by a comma and a space.
# Insert "and" before last item and check single and empty list [].

# Example List
spam = ['apples', 'bananas', 'tofu', 'cats','dog',6,6.5,'humans']


def printList(list):
    if len(list) == 0:
        print('Please enter a full list')
    elif len(list) == 1:
      print("Only {}.".format(list[0]))
    else:
      for items in list:
        if list.index(items) != len(list)-1:
          print("{}, ".format(items),end="")
        else:
          print("and {}.".format(items),end="")

printList(spam)
