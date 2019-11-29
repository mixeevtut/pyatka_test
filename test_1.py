import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_1():
    phone = 9057199558
    card = 7789004125415905
    url = 'https://5ka:eish7ohzo5Esh@mystage.5ka.ru/login'
    password = '5ka5ka'
    code = '0000'

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_1(self):
        self.first_factor_auth_card()
        time.sleep(2)
        self.second_factor_auth()
        time.sleep(3)

    def first_factor_auth_phone(self):
        self.driver.get(Test_1.url)
        time.sleep(2)
        self.driver.set_window_size(1920, 1057)
        self.driver.find_element(By.ID, "authPhone").send_keys(Test_1.phone)
        self.driver.find_element(By.NAME, "phone_password").send_keys(Test_1.password)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) .form__submit-button").click()

    def first_factor_auth_card(self):
        self.driver.get(Test_1.url)
        time.sleep(1)
        self.driver.set_window_size(1920, 1057)
        self.driver.find_element(By.CSS_SELECTOR, ".tabs__item:nth-child(2) > .tabs__item-name").click()
        self.driver.find_element(By.ID, "authCard").send_keys(Test_1.card)
        self.driver.find_element(By.NAME, "cardNo_password").send_keys(Test_1.password)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .form__submit-button").click()

    def second_factor_auth(self):
        self.driver.find_element(By.NAME, "code").click()
        self.driver.find_element(By.NAME, "code").send_keys(Test_1.code)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".form__submit-button").click()
