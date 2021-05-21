# Updatable Multi-Clipboard
# Program takes a command line argument and/or a keyword
# If the argument is save, clipboard contents are saved to the keyword.
# If the argument is list, all keywords/definitions are listed
# If the argument is delete, then the keyword is deleted from the clipboard.
# Otherwise, the text for the keyword is copied to the clipboard.

import pyperclip, shelve
import sys

# Create new data shelve
mcbShelf = shelve.open('mcb')

def update_clipboard():
  responce = "Please provide a Keyword."
  if len(sys.argv) == 2:
    argument = sys.argv[1].lower()
    if argument == 'list':
      return list(mcbShelf.items())
    else:
      # If there is no command check if the keyword exist in the shelf, then copy to the paperclip
      if argument in mcbShelf.keys():
        pyperclip.copy(mcbShelf[argument])
        responce = 'The keyword has been copied'
      else:
        responce = 'This keyword has not been recorded.'
  
  elif len(sys.argv) == 3:
    keyword = sys.argv[2].lower()
    argument = sys.argv[1]
    if argument == 'save':
      # Check if keyword is already saved, if not ask to override current definition
        if keyword in mcbShelf.keys():
          print('This keyword is already recorded as {}'.format(mcbShelf[keyword]))
          answer = input('Would you like to overide it Y/N?: ')
          if answer.lower() == 'y':
            mcbShelf[keyword] = pyperclip.paste()
            return "{} saved as {}".format(keyword,mcbShelf[keyword])
          else:
              return '{} will remain as: {}'.format(keyword,mcbShelf[keyword])
        else:
            mcbShelf[keyword] = pyperclip.paste()
            return "{} saved as {}".format(keyword,mcbShelf[keyword])
    # The option is given to delete the selected keyword or the entire database      
    elif  argument == 'delete':
      if sys.argv[2].lower() in mcbShelf.keys():
        answer = input('Would you like to delete selected keyword or clear all entries? keyword/all: ')
        if answer.lower() == 'keyword':
          del mcbShelf[keyword]
          return '{} has been removed.'.format(keyword)
        elif answer.lower() == 'all':
          mcbShelf.clear()
          return 'The data base has been cleared.'
      else:
        responce = 'Please include a keyword.'
  return responce
  

if __name__ == "__main__":
  print( update_clipboard() )
  # Close the shelve
  mcbShelf.close() 