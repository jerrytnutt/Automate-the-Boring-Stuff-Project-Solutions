# Updatable Multi-Clipboard
# The command line argument for the keyword is checked.
# If the argument is save, then the clipboard contents are saved to the keyword.
# If the argument is list, then all the keywords are copied to the clipboard.
# If the argument is delete, then the keyword is deleted frm the clipboard.
# Otherwise, the text for the keyword is copied to the clipboard.

import pyperclip, shelve
import sys

# Create new data shelve
mcbShelf = shelve.open('mcb')

# Check length of sys.argv for clipboard action
def update_clipboard():
  responce = None
  if len(sys.argv) == 2:
    argument = sys.argv[1].lower()
    if argument == 'list':
      return list(mcbShelf.items())
    else:
      # If there is no command check if the keyword exist in the shelf, then copy to the paperclip
      if argument in mcbShelf.keys():
        return pyperclip.copy(mcbShelf[argument])
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
        answer = input('Would you like to delete selected keyword or clear all entries? Keyword/All: ')
        if answer.lower() == 'keyword':
          del mcbShelf[keyword]
          return '{} has been removed.'.format(keyword)
        elif answer.lower() == 'all':
          mcbShelf.clear()
          return 'The data base has been cleared.'
      else:
        responce = 'Please include a keyword.'

  else:
    responce = 'Please include a keyword.'
  return responce
  

if __name__ == "__main__":
  print( update_clipboard() )
  # Close the shelve
  mcbShelf.close() 




