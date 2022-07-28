import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class ChromeTest(unittest.TestCase):

    def setUp(self):
        s = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test_success_login(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('Hoffa368')
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('imbaimba!23')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        name_acc = driver.find_element(
            By.XPATH, "//div[@CLASS='personal-info-login__text personal-info-login__text_decorated']").text

        assert name_acc == "Hoffa368"

    def test_failure_login(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(By.XPATH, "//input[@CLASS='Textinput-Control']")
        time.sleep(1)
        elem.send_keys('Hoffa368')
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

        print(text_message)

        assert text_message == "Неверный пароль"


if __name__ == '__main__':
    unittest.main()