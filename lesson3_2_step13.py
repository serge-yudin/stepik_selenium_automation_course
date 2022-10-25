import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWeb(unittest.TestCase):
    def test_first_link(self):
        url = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(url)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(
            By.CSS_SELECTOR, 'div.first_block div.first_class input').send_keys('IVAN')
        browser.find_element(
            By.CSS_SELECTOR, 'div.first_block div.second_class input').send_keys('IVAN')
        browser.find_element(
            By.CSS_SELECTOR, 'div.first_block div.third_class input').send_keys('IVAN')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        # input()
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_second_link_should_fail(self):
        url = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(url)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(
            By.CSS_SELECTOR, 'div.first_block div.first_class input').send_keys('IVAN')
        browser.find_element(
            By.CSS_SELECTOR, 'div.first_block div.second_class input').send_keys('IVAN')
        browser.find_element(
            By.CSS_SELECTOR, 'div.first_block div.third_class input').send_keys('IVAN')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        # input()
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # закрываем браузер после всех манипуляций
        browser.quit()

    # def test_abc(self):
    #    self.assertEqual(3*4, 12*1)


if __name__ == '__main__':
    unittest.main()
