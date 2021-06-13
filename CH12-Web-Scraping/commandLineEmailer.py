from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, sys

def send_email(email,password,message):
  driver = webdriver.Chrome(ChromeDriverManager().install())
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver.get("https://mail.tutanota.com/")
  
  try: 
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='email']"))).send_keys(email)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='password']"))).send_keys(password)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.limit-width"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[title='New email']"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='text']"))).send_keys(email)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[aria-label='Subject']"))).send_keys(message)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[aria-multiline='true']"))).send_keys(message)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[title='Send']"))).click()
    time.sleep(5)
    driver.quit()
  except Exception as e:
    print(repr(e))
    driver.quit()
  return None

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print('Please provide a email address, password and message')
  else:
    email = sys.argv[1] 
    password = sys.argv[2]
    message = ' '.join(sys.argv[3:])
    print("Email: ",email)
    print("Password: ",password)
    print("Message: ",message)
    send_email(email,password,message)