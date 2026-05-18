from unittest.mock import Mock, patch

import httpx
import pytest

from py_connect_test.services.http import HttpTest


@pytest.fixture
def mock_http_settings():
    with patch("py_connect_test.services.http.HttpSettings") as mock:
        instance = Mock()
        instance.url = "https://example.com"
        mock.return_value = instance
        yield instance


@pytest.fixture
def mock_alert_settings():
    with patch("py_connect_test.services.http.AlertSettings") as mock:
        instance = Mock()
        instance.webhook_url = "http://webhook.local"
        instance.payload_file_path = "payload.json"
        mock.return_value = instance
        yield instance


@pytest.fixture
def mock_logger():
    with patch("py_connect_test.services.http.logger") as mock:
        yield mock


@pytest.fixture
def http_test_instance(mock_http_settings, mock_alert_settings, mock_logger):
    return HttpTest(insecure=False)


@pytest.fixture
def mock_response():
    response = Mock(spec=httpx.Response)
    response.status_code = 200
    response.text = '{"status": "ok"}'
    response.json.return_value = {"status": "ok"}
    return response
