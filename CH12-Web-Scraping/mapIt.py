# Gets a street address from the command line arguments or clipboard
# Open the web browser to Google Maps for that address
# Call webbrowser.open() function to open the web browser

import webbrowser, sys, pyperclip
# Check the length of the command line arguments
if len(sys.argv) > 1:
  address = sys.argv[1:]
  address = ' '.join(sys.argv[1:])
# If no command line argument is available use the paperclip argument
else:
    address = pyperclip.paste()

link = 'https://www.google.com/maps/place/'+address
webbrowser.open(link)