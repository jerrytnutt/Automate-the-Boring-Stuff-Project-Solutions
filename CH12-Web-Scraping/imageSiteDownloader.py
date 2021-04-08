# Image Site Downloader
# Program that goes to a photo-sharing site like Flickr or Imgur 
# Searches for a category of photos, and downloads all the resulting images

import sys, webbrowser, requests, os
from bs4 import BeautifulSoup

# Path to folder to save files files
path = 'path'

def download_images(search_term):
  # main_page will be imgur's search results for top scoring photos of all time
  main_page = 'https://imgur.com/search/score/all?q='+search_term+'&qs=thumbs'
  res = requests.get(main_page)
  res.raise_for_status
  soup = BeautifulSoup(res.text, 'html.parser')

  # Search for all the image links on the page
  images = soup.find_all('a', class_='image-list-link')

  for i in range(len(images)):
    # Remove letter "b" from each url to improve quality of image
    image_url = 'https:'+images[i].img['src'][:21] + images[i].img['src'][22:]
    img_data = requests.get(image_url).content

    # Give the image a path and write the file to download
    filename = 'image'+str(i)+'.jpg'
    location = os.path.join(path,filename)
    
    with open(location, 'wb') as handler:
      handler.write(img_data)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    search_term = sys.argv[1:]
    search_term  = ' '.join(sys.argv[1:])
    download_images(search_term)
  else:
    print("Please enter a search term for the site")  