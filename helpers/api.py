import requests
from config import settings


class ApiClient:
    """
    Обёртка над API приложения.
    Держит requests.Session и токен авторизации.
    """

    def __init__(self, api_url: str, session: requests.Session | None = None):
        self.base = api_url.rstrip("/")
        self.http = session or requests.Session()
        self.token = None

    def _url(self, path: str) -> str:
        return f"{self.base}{path}"

    # --------------------------
    # Базовые эндпоинты
    # --------------------------

    def health(self):
        """GET /health — проверка доступности сервиса"""
        return self.http.get(self._url(settings.ep_health))

    def register(self, full_name: str, email: str, password: str):
        """POST /auth/register — регистрация пользователя"""
        payload = {"full_name": full_name, "email": email, "password": password}
        return self.http.post(self._url(settings.ep_register), json=payload)

    def login(self, email: str, password: str):
        """POST /auth/login — логин, сохранение токена"""
        r = self.http.post(
            self._url(settings.ep_login),
            json={"email": email, "password": password}
        )
        if r.ok and "access_token" in r.json():
            self.token = r.json()["access_token"]
            self.http.headers.update({"Authorization": f"Bearer {self.token}"})
        return r

    def me_get(self):
        """GET /me — получить профиль текущего пользователя"""
        return self.http.get(self._url(settings.ep_me))

    def me_patch(self, payload: dict):
        """PATCH /me — изменить профиль"""
        return self.http.patch(self._url(settings.ep_me), json=payload)

    # --------------------------
    # Админские эндпоинты
    # --------------------------

    def admin_user_create(self, payload: dict):
        """
        POST /admin/users — создать пользователя от имени админа.
        Ожидается JSON вида {"full_name": ..., "email": ..., "password": ...}
        """
        return self.http.post(self._url(settings.ep_admin_user), json=payload)
