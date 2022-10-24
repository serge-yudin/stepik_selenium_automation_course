import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson6_step4 import fill_form

browser = webdriver.Chrome()

url = 'http://suninjuly.github.io/find_link_text'

browser.get(url)
link = browser.find_element(By.LINK_TEXT, str(
    math.ceil(math.pow(math.pi, math.e)*10000)))

link.click()

#print(type(page), browser.current_url)
input1 = browser.find_element(By.NAME, 'first_name')
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, 'city')
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
input()
browser.quit()
