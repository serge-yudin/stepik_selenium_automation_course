from time import sleep
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    '''ln(abs(12*sin(x)))'''
    # return math.log10(abs(12 * math.sin(int(x))))
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    x = browser.find_element(By.ID, 'input_value').text
    print(type(x), x)
    browser.execute_script('window.scrollBy(0,200);')
    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    sleep(15)
    browser.quit()
