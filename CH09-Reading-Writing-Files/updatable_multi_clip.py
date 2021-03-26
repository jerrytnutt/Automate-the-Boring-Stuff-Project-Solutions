# Updatable Multi-Clipboard
# The command line argument for the keyword is checked.
# If the argument is save, then the clipboard contents are saved to the keyword.
# If the argument is list, then all the keywords are copied to the clipboard.
# If the argument is delete, then the keyword is deleted frm the clipboard.
# Otherwise, the text for the keyword is copied to the clipboard.

import pyperclip, shelve
import sys

#Create new data shelve
mcbShelf = shelve.open('mcb')


#check length of sys.argv for clipboard action
def update_clipboard():
  if len(sys.argv) == 2:
    argument = sys.argv[1].lower()
    if argument == 'list':
        print(list(mcbShelf.items()))
    else:
      # If there is no command check if the keyword exist in the shelf, then copy to the paperclip
      if argument in mcbShelf.keys():
        pyperclip.copy(mcbShelf[argument])
      else:
        print('This keyword has not been recorded')
  
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
            print("{} saved as {}".format(keyword,mcbShelf[keyword]))
          else:
              print('{} will remain as: {}'.format(keyword,mcbShelf[keyword]))
        else:
            mcbShelf[keyword] = pyperclip.paste()
            print("{} saved as {}".format(keyword,mcbShelf[keyword]))
    # The option is given to delete the selected keyword or the entire database      
    elif  argument == 'delete':
      if sys.argv[2].lower() in mcbShelf.keys():
        answer = input('Would you like to delete selected keyword or clear all entries? Keyword/All: ')
        if answer.lower() == 'keyword':
          print(keyword)
          del mcbShelf[keyword]
        elif answer.lower() == 'all':
          mcbShelf.clear()
      else:
    print('Please include a keyword.')

  else:
    print('Please include a keyword.')
  # Close the shelve
  mcbShelf.close()
  

if __name__ == "__main__":
  update_clipboard()  




