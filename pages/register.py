from selenium.webdriver.common.by import By
from .base import BasePage


class RegisterPage(BasePage):
    PATH = "/register"

    FULL_NAME = (By.CSS_SELECTOR, 'input[name="full_name"], input[name="fio"]')
    EMAIL = (By.CSS_SELECTOR, 'input[name="email"], input[type="email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT = (By.XPATH, '//button[normalize-space()="Register" or @type="submit"]')

    def register(self, full_name: str, email: str, password: str):
        self.open()
        self.wait_visible(self.FULL_NAME).send_keys(full_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()
        return self
