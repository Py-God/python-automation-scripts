#! python3
# goes to the copyblogger site and comments on 3 of their blogs (first 3)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.implicitly_wait(20)
browser.get('https://copyblogger.com/')
time.sleep(2)

posts = browser.find_elements(By.CLASS_NAME, 'entry-title-link')

for i in range(len(posts)):
    posts = browser.find_elements(By.CLASS_NAME, 'entry-title-link')
    posts[i+2].click()
    time.sleep(2)
    page = browser.find_element(By.TAG_NAME, 'html')
    page.send_keys(Keys.END)

    commentSection = browser.find_element(By.ID, 'comment')
    commentSection.send_keys('Lovely article')
    time.sleep(2)
    nameSection = browser.find_element(By.ID, 'author')
    nameSection.send_keys('Random_Dude')
    time.sleep(2)
    EmailSection = browser.find_element(By.ID, 'email')
    EmailSection.send_keys('RandomDude@gmail.com')
    time.sleep(2)
    submitButton = browser.find_element(By.NAME, 'submit')
    submitButton.click()

    browser.back()
    browser.back()
browser.quit()