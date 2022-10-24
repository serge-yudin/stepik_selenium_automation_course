import time

from selenium import webdriver
from selenium.webdriver.common.by import By



def test_registration(url):
    try:

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
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':

    # Запустятся поочередно тест на регистрацию по первой ссылке, затем по второй.
    # Первый тест проходит, второй выбрасывает исключение selenium.common.exceptions.NoSuchElementException
    urls = ["http://suninjuly.github.io/registration1.html",
            "http://suninjuly.github.io/registration2.html"]

    for url in urls:
        test_registration(url)

