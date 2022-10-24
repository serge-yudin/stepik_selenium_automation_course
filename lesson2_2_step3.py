import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

'''
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
'''

url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    sum_ = int(browser.find_element(By.ID, 'num1').text) + \
        int(browser.find_element(By.ID, 'num2').text)
    print(sum_)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    print(type(select), select)
    select.select_by_value(str(sum_))
    #browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    js = '''document.title='Test of JS';
    alert("JS in Selenium");
    console.log('hey there');
    '''
    browser.execute_script(js)
finally:
    time.sleep(25)
    browser.quit()
