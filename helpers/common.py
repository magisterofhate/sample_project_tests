# -*- coding: utf-8 -*-
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Common:

    def __init__(self, app):
        self._app = app

    def insert_text(self, locator, text):
        self._app.wd.find_element(By.XPATH, locator).send_keys(text)

    def clear_field(self, locator):
        self.click_element(locator)
        self._app.wd.find_element(By.XPATH, locator).clear()

    def clear_field_hard_way(self, locator):
        self._app.wd.find_element(By.XPATH, locator).send_keys(Keys.CONTROL + "a")
        self._app.wd.find_element(By.XPATH, locator).send_keys(Keys.DELETE)

    def click_element(self, locator):
        self.wait_for_element(locator)

        for i in range(4):
            try:
                self._app.wd.find_element(By.XPATH, locator).click()
                break
            except StaleElementReferenceException:
                print('Stale Element occurred')

    def wait_for_element(self, locator, timeout=20, poll_fqc=0.2):
        wait = WebDriverWait(self._app.wd, timeout=timeout, poll_frequency=poll_fqc)
        wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
