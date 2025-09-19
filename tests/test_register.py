import pytest
import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.register import RegisterPage

pytestmark = [pytest.mark.ui, pytest.mark.ui_selenium, pytest.mark.smoke]


@allure.feature("Auth")
@allure.story("Register")
def test_user_registration_via_selenium(app):
    fake = Faker()

    full_name = "Тест Пользователь"
    email = fake.unique.email()
    password = "Test1234"  # 6–18 символов, латиница/цифры/допустимые спецсимволы

    with allure.step("Открываем страницу регистрации и заполняем форму"):
        reg = RegisterPage(app.wd, app.base_url).open()
        reg.register(full_name=full_name, email=email, password=password)

    with allure.step("Ожидаем индикатор успеха (редирект/сообщение/ссылки навигации)"):
        wait = WebDriverWait(app.wd, 10)

        message = app.wd.find_element(By.XPATH, "//article[@class='card']/descendant::p").text

        assert message == 'Регистрация успешна. Войдите в систему.', 'Регистрация неуспешна!'

