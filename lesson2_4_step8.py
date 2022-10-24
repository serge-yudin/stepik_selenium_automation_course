import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

book_btn = 'book'
price = 'price'
xval = 'input_value'
answer = 'answer'
submit = 'solve'

url = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


browser = webdriver.Chrome()
browser.get(url)
book = browser.find_element(By.ID, book_btn)
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
book.click()
x = browser.find_element(By.ID, xval).text
browser.find_element(By.ID, answer).send_keys(calc(x))
browser.find_element(By.ID, submit).click()
res = browser.switch_to.alert.text
print(res)
