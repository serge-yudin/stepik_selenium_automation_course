import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('page', links)
def test_open_page(browser, page):
    browser.implicitly_wait(5)
    browser.get(page)

    WebDriverWait(browser, 8).until(EC.title_contains('Step 1'))
    answer = math.log(int(time.time()))
    browser.find_element(
        By.CSS_SELECTOR, 'textarea.ember-text-area').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.attempt__message p')))
    assert browser.find_element(
        By.CSS_SELECTOR, '.attempt__message p').text == 'Correct!'
