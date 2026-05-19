import json

import httpx

from py_connect_test.settings import AlertSettings, HttpSettings
from py_connect_test.setup_logger import setup_logger

logger = setup_logger()


class HttpTest:
    def __init__(self, insecure: bool) -> None:
        self.http_settings = HttpSettings()
        self.alert_settings = AlertSettings()
        self.insecure = insecure

    def get(self) -> httpx.Response:
        with httpx.Client(
            base_url=self.http_settings.url,
            verify=not self.insecure,
        ) as client:
            response = client.get("/")
            response.raise_for_status()
            return response

    def get_status_code(self) -> int:
        response = self.get()
        return response.status_code

    def post_alerts(self) -> httpx.Response:
        with open(self.alert_settings.payload_file_path) as f:
            payload = json.load(f)

        with httpx.Client(
            base_url=self.alert_settings.webhook_url,
            verify=not self.insecure,
        ) as client:
            response = client.post("/", json=payload)
            response.raise_for_status()
            logger.success(
                f"Alert posted successfully to {self.alert_settings.webhook_url}",
            )
            return response
