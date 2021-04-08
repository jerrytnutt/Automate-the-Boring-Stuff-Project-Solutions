# Opening All Search Results
# Read the command line arguments from sys.argv
# Fetch the search result page with the requests module
# Find the links to each search result and open with webbrowser.open()
 
import sys, webbrowser, requests
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
    results = ' '.join(sys.argv[1:])
    # Download and parse the main page
    mainPage = 'https://pypi.org/search/?q='+results
    page = requests.get(mainPage)
    src = page.content
    soup = BeautifulSoup(page.content, 'html.parser')
    # Grab all of the list elements under ul
    ul = soup.find_all("ul", class_="unstyled")
    li = ul[0].find_all('li')
    # Use min() for arguments that may contain < 5 links
    linksToOpen = min(5, len(li))
    # Grab the a['href'] from each lik and then open them in the webrowser
    for i in range(linksToOpen):
      link = 'https://pypi.org/search/?q='+li[i].a['href']
      print("Opening Link for {}".format(link))
      webbrowser.open(link)
        
else:
    print('Please supply an argument')