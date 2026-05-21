from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PY_CONNECT_TEST_")

    url: str = "https://ifconfig.me"


class AlertSettings(BaseSettings):
    webhook_url: str = "http://prometheus.local"
    payload_file_path: str = "payload.json"
