from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PY_CONNECT_TEST_")

    url: str = "https://ntfy.me"


class AlertSettings(BaseSettings):

    webhook_url: str = "http://prometheus.local"
    payload_file_path: str = "/app/src/py_connect_test/templates/alertmanager-payload.json"
