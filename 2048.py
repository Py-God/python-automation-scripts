# python3
# Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up
# right, down, and left keystrokes to automatically play the game
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.implicitly_wait(20)
browser.get('https://gabrielecirulli.github.io/2048/')

EntirePage = browser.find_element(By.TAG_NAME, 'html')
while True:
    EntirePage.send_keys(Keys.UP)
    time.sleep(1)
    EntirePage.send_keys(Keys.RIGHT)
    time.sleep(1)
    EntirePage.send_keys(Keys.DOWN)
    time.sleep(1)
    EntirePage.send_keys(Keys.LEFT)
    time.sleep(1)
    try:
        retryButton = browser.find_element(By.CLASS_NAME, 'retry-button')
        break
    except:
        continue
