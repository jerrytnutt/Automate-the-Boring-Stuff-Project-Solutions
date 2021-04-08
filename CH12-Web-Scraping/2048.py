# 2048
# Write a program that will open the 2048 game  
# Keep sending keystrokes to automatically play the game

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

# Use chromedriver to access the site with chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://play2048.co")

try: 
  # List of four possible moves
  move_list = [Keys.LEFT, Keys.DOWN, Keys.RIGHT, Keys.UP]
  for i in range(20):
    # One second sleep delay so moves are not instantaneous
    sleep(1)
    # Access the body and randomly select a move
    driver.find_element_by_css_selector('body').send_keys(random.choice(move_list))

  # After all turns the game is reset and the driver is closed
  
  driver.find_element_by_class_name('restart-button').click()
  driver.quit()
except:
  print('error')
  driver.quit()