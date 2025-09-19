from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


class BasePage:
    PATH = "/"

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self):
        """Открыть страницу по self.PATH"""
        self.driver.get(self.base_url + self.PATH)
        return self

    def wait_visible(self, locator):
        """Ждать, пока элемент станет видимым"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def current_url(self) -> str:
        return self.driver.current_url
