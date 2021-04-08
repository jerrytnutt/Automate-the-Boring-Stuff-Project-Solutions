# Loads the XKCD home page and saves the comic image
# Follows the Previous Comic link and repeats until it reaches the first comic

import sys, webbrowser, requests, os
from bs4 import BeautifulSoup

os.makedirs('xkcd', exist_ok=True)  

# xkcd starting page URL
url = "https://xkcd.com"
itteration = 1

# While loop runs until it reaches first comic
while not url.endswith('#'):
  # Download the current page
  res = requests.get(url)
  print('Downloading page... {}'.format(url))
  res.raise_for_status()

  # Use BeautifulSoup to locate the URL for the page's image
  soup = BeautifulSoup(res.text, 'html.parser')
  comicdiv = soup.find("div", id="comic")

  if comicdiv == []:
        print('Could not find comic image.')
  else:
    # Download the image
    imageData = 'https:' + comicdiv.img['src']
    print('Downloading image... {}'.format(imageData))
    res = requests.get(imageData)
    res.raise_for_status()

  # Create a file name and path for each image
  filename = "xkcd" + str(itteration) + ".png"
  newpath = os.path.join('xkcd', filename)
  
  # Write the content into a file
  with open(newpath, 'wb') as handler:
    for chunk in res.iter_content(100000):
      handler.write(chunk)

  # Update the url with the previous pages link
  itteration = itteration + 1
  prevLink = soup.select('a[rel="prev"]')[0]
  url = 'https://xkcd.com' + prevLink.get('href')

print("Complete...")
