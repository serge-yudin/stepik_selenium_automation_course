import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    valuex = browser.find_element(
        By.CSS_SELECTOR, 'h2 img').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(valuex))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(20)
    browser.quit()
