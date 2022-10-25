

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='class')
def browser():
    print('\n\tstart browser for test ...')
    browser = webdriver.Chrome(options=options)  # browser
    yield browser
    print('\n\tclosing browser browser.quit()')
    browser.quit()

class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')


