import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(x)))


url = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    first = browser.window_handles[-1]
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    second = browser.window_handles[-1]
    browser.switch_to.window(second)
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()
