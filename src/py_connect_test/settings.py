from pydantic_settings import BaseSettings


class HttpSettings(BaseSettings):
    url: str = "https://ifconfig.me"

    class Config:
        prefix = "py_connect_test"


class AlertSettings(BaseSettings):
    webhook_url: str = "http://prometheus.local"
    payload_file_path: str = "payload.json"
