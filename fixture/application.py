# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import warnings
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeO

from helpers.common import Common
from helpers.navigation import Navigation
from helpers.search_helper import SearchHelper


class Application:

    def __init__(self, browser="chrome", base_url="http://45.150.8.53/"):
        self.browser = browser
        self.wd = None
        self.select = None
        self.navigation = Navigation(self)
        self.common = Common(self)
        self.search = SearchHelper(self)
        self.base_url = base_url

    def initialize(self):
        if self.browser == "ff":
            options = Options()
            options.headless = True
            self.wd = webdriver.Firefox(options=options)
        elif self.browser == "chrome":
            options = ChromeO()
            # options.add_argument('--headless')
            # options.add_argument('--no-sandbox')
            # options.add_argument('--disable-gpu')
            # options.add_argument("--width=1920")
            # options.add_argument("--height=700")
            options.add_argument("--window-size=1600,1024")
            self.wd = webdriver.Chrome(options=options)
            # self.wd = webdriver.Chrome()
        else:
            warnings.warn("Unrecognized browser %s. Used default" % self.browser, Warning)
            self.wd = webdriver.Chrome()
        self.select = webdriver.support.ui.Select
        self.wd.get("http://45.150.8.53/")

    def destroy(self):
        self.navigation.logout()
        self.wd.quit()