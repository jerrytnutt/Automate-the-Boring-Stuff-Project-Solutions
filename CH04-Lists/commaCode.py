# Comma Code
# A function that takes a list and returns a string with all items separated by a comma and a space.
# Insert "and" before last item and check single and empty list [].

spam = ['apples', 'bananas', 'tofu', 'cats']

def create_string(list):
  new_list = ''
  if len(list) == 0:
    new_list = 'Please enter a full list'
  elif len(list) == 1:
    new_list = "Only {}.".format(list[0])
  else:
    for items in list:
      if list.index(items) != len(list)-1:
        new_list += "{}, ".format(items)
      else:
        new_list += "and {}.".format(items)
  return new_list

if __name__ == '__main__':
  print( create_string(spam) )