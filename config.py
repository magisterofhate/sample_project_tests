from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    # базовый URL приложения
    base_url: str = os.getenv("BASE_URL", "http://45.150.8.53/")
    api_docs: str = os.getenv("API_DOCS", "http://45.150.8.53/api/v1/")

    # учётка администратора для фикстур и тестов
    admin_email: str = os.getenv("ADMIN_EMAIL", "admin@example.com")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "SuperSecret123")

    # режим запуска UI-тестов
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"

    # эндпоинты приложения (можно переопределять переменными окружения)
    ep_health: str = os.getenv("EP_HEALTH", "/health")
    ep_login: str = os.getenv("EP_LOGIN", "/login")
    ep_register: str = os.getenv("EP_REGISTER", "/register")
    ep_me: str = os.getenv("EP_ME", "/me")                      # GET/PATCH
    ep_admin_user: str = os.getenv("EP_ADMIN_USER", "/admin/users")  # POST


# глобальный объект настроек
settings = Settings()
