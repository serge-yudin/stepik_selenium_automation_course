import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:

    browser.get(url)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x)))
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(30)
    browser.quit()
