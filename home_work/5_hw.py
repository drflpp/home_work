from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

text_username = driver.find_element(By.CSS_SELECTOR, '[id="user-name"]')
text_password = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
button_submit = driver.find_element(By.CSS_SELECTOR, '[id="login-button"]')

if text_username and text_password and button_submit:
    print('Elements are found')