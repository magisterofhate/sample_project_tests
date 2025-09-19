import pytest
from helpers.api import ApiClient
from config import settings


@pytest.mark.api
def test_admin_login_and_me():
    api = ApiClient(settings.api_docs)

    # Логинимся админом
    r_login = api.login(settings.admin_email, settings.admin_password)
    assert r_login.status_code == 200, f"Login failed: {r_login.status_code} {r_login.text}"

    # Проверяем, что залогинились: дергаем /me
    r_me = api.me_get()
    assert r_me.status_code == 200, f"/me failed: {r_me.status_code} {r_me.text}"
    me = r_me.json()
    assert me.get("email") == settings.admin_email, f"Ожидали email {settings.admin_email}, а получили {me}"
