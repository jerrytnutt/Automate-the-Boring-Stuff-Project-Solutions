# 1. The command line argument for the keyword is checked.
# 2. If the argument is save, then the clipboard contents are saved to the keyword.
# 3. If the argument is list, then all the keywords are copied to the clipboard.
# 4. Otherwise, the text for the keyword is copied to the clipboard.
# 5. Extend the multi-clipboard program in this chapter so that it has a delete <keyword> command line argument
# 6. Add a delete command line argument that will delete all keywords.

import pyperclip
import sys
import shelve

#Create new data shelve
mcbShelf = shelve.open('mcb')


sysArg1 = sys.argv[1]

#check length of sys.argv for clipboard action
if len(sys.argv) == 2:
  keyword = sys.argv[1]
  if sysArg1.lower() == 'list':
      print(list(mcbShelf.items()))
  else:
    # If there is no command check if the keyword exist in the shelf, then copy to the paperclip
    if keyword in mcbShelf.keys():
      pyperclip.copy(mcbShelf[keyword])
    else:
      print('This keyword has not been recorded')

elif len(sys.argv) == 3:
  keyword = sys.argv[2]
  if sysArg1.lower() == 'save':
    # Check if keyword is already saved, if not ask to override current definition
      if keyword in mcbShelf.keys():
        print('This keyword is already recorded as {}'.format(mcbShelf[keyword]))
        answer = input('Would you like to overide it y/n?: ')
        if answer == 'y':
          content = pyperclip.paste()
          mcbShelf[keyword] = content
          print("{} saved as {}".format(keyword,mcbShelf[keyword]))
        else:
            print('{} will remain as: {}'.format(keyword,mcbShelf[keyword]))
      else:
          content = pyperclip.paste()
          mcbShelf[keyword] = content
          print("{} saved as {}".format(keyword,mcbShelf[keyword]))
  # The option is given to delete the selected keyword or the entire database      
  elif  sysArg1.lower() == 'delete': 
    answer = input('Would you like to delete selected keyword or clear all entries? keyword/all: ')
    if answer == 'keyword':
      del mcbShelf[keyword]
    elif answer == 'all':
      mcbShelf.clear()
    


# Close the shelve
mcbShelf.close()
  




