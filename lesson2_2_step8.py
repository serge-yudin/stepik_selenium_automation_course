from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="firstname"]').send_keys('Tester')
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="lastname"]').send_keys('Testerov')
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(
        'test@tester.com')
    browser.find_element(By.ID, 'file').send_keys(os.path.join(os.getcwd(), 'test.txt'))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    sleep(25)
    browser.quit()