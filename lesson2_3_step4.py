import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(x)))


url = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, '.container button').click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    res = browser.switch_to.alert.text.split(': ')[-1]
    print(res)
finally:
    browser.quit()
