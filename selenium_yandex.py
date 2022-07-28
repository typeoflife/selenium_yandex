import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random


class ChromeTest(unittest.TestCase):

    def setUp(self):
        s = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test_success_login(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('my_login')
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('my_password')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        name_acc = driver.find_element(
            By.XPATH, "//div[@CLASS='personal-info-login__text personal-info-login__text_decorated']").text

        assert name_acc == "my_account_name"

    def test_failure_login(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('my_login')
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('wrong_password')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        text_message = driver.find_element(
            By.XPATH, "//div[@CLASS='Textinput-Hint Textinput-Hint_state_error']").text

        assert text_message == "Неверный пароль"

    def test_yandex_follow(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        driver.find_element(By.XPATH, "//a[@CLASS='Logo Logo_ya']").click()
        time.sleep(2)
        try:
            finder = driver.find_element(
                By.XPATH, "//input[@CLASS='input__control input__input mini-suggest__input']")
        except NoSuchElementException:
            return False

        assert finder

    def test_yandex_create_button(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        time.sleep(1)
        try:
            driver.find_element(
                By.XPATH, "//button[@CLASS='Button2 Button2_size_l Button2_view_clear']").click()
            imput_tel = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
            imput_tel.send_keys(f'+5{random.randrange(1111111111, 9999999999, 10)}')
            imput_tel.send_keys(Keys.RETURN)
            text_message = driver.find_element(
                By.XPATH, "//div[@CLASS='Textinput-Hint Textinput-Hint_state_error']").text


        except NoSuchElementException:
            return False

        assert text_message


if __name__ == '__main__':
    unittest.main()
