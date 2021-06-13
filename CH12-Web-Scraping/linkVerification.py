# Link Verification
# Program takes the URL of a web page and attempts to download every linked page on the page 
# Program flags any pages that have 404 “Not Found” status code

import sys, webbrowser, requests, os
from bs4 import BeautifulSoup
def verify_links(main_page):
  # Main Page that will be searched for links

  res = requests.get(main_page)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'html.parser')
  
  # Find all links on main_page
  linked_pages = soup.find_all('a')

  hyper = 'https://'
  for links in linked_pages:
    # Traverse the links and check for status code
    try:
      if hyper in links['href']:
        url = links['href']
        new_request = requests.get(url)
        res.raise_for_status()
        print(url)
        print(new_request.status_code)
    except:
      print("404 status code {} is broken".format(url))
  return main_page
  
if __name__ == '__main__':
  verify_links('https://www.georgiaaquarium.org/') 