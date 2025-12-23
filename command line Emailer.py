#! python3
# Write a program that takes an email address and string of text on the command line and then,
# using Selenium, logs into your email account and sends an email of the string to the provided address.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.implicitly_wait(20)
browser.get('https://mail.google.com/')

emailElem = browser.find_element(By.ID, 'identifierId')
emailElem.send_keys('boluwatifelekeoduoye@gmail.com')
nextElem = browser.find_element(By.ID, 'identifierNext')
nextElem.click()
