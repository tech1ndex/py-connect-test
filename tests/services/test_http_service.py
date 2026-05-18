import json
from unittest.mock import MagicMock, mock_open, patch

import httpx
import pytest

from py_connect_test.services.http import HttpTest


class TestHttpTestInit:
    def test_init_with_insecure_false(self, http_test_instance):
        assert http_test_instance.insecure is False

    def test_init_with_insecure_true(self):
        with patch("py_connect_test.services.http.HttpSettings"), patch(
            "py_connect_test.services.http.AlertSettings",
        ):
            http_test = HttpTest(insecure=True)
            assert http_test.insecure is True

    def test_init_creates_settings(
        self,
        http_test_instance,
        mock_http_settings,
        mock_alert_settings,
    ):
        assert http_test_instance.http_settings == mock_http_settings
        assert http_test_instance.alert_settings == mock_alert_settings


class TestHttpTestGet:
    @patch("py_connect_test.services.http.httpx.Client")
    def test_get_success(self, mock_client_class, http_test_instance, mock_response):
        mock_client = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        response = http_test_instance.get()

        assert response == mock_response
        mock_client.get.assert_called_once_with("/")

    @patch("py_connect_test.services.http.httpx.Client")
    def test_get_uses_correct_base_url(
        self,
        mock_client_class,
        http_test_instance,
        mock_response,
    ):
        mock_client = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        http_test_instance.get()

        mock_client_class.assert_called_once_with(
            base_url=http_test_instance.http_settings.url,
            verify=True,
        )

    @patch("py_connect_test.services.http.httpx.Client")
    def test_get_respects_insecure_flag(self, mock_client_class, mock_response):
        with patch("py_connect_test.services.http.HttpSettings"), patch(
            "py_connect_test.services.http.AlertSettings",
        ):
            http_test = HttpTest(insecure=True)
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value.__enter__.return_value = mock_client

            http_test.get()

            mock_client_class.assert_called_once_with(
                base_url=http_test.http_settings.url,
                verify=False,
            )

    @patch("py_connect_test.services.http.httpx.Client")
    def test_get_raises_on_bad_status(self, mock_client_class, http_test_instance):
        mock_client = MagicMock()
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found",
            request=MagicMock(),
            response=mock_response,
        )
        mock_client.get.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        with pytest.raises(httpx.HTTPStatusError):
            http_test_instance.get()


class TestHttpTestGetStatusCode:
    def test_get_status_code_returns_code(self, http_test_instance, mock_response):
        with patch.object(http_test_instance, "get", return_value=mock_response):
            status_code = http_test_instance.get_status_code()
            mock_success_code = 200

            assert status_code == mock_success_code

    def test_get_status_code_calls_get(self, http_test_instance, mock_response):
        with patch.object(
            http_test_instance,
            "get",
            return_value=mock_response,
        ) as mock_get:
            http_test_instance.get_status_code()

            mock_get.assert_called_once()


class TestHttpTestPostAlerts:
    @patch("py_connect_test.services.http.httpx.Client")
    def test_post_alerts_success(
        self,
        mock_client_class,
        http_test_instance,
        mock_response,
    ):
        payload = {"alert": "test"}

        mock_client = MagicMock()
        mock_client.post.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        with patch("builtins.open", mock_open(read_data=json.dumps(payload))):
            response = http_test_instance.post_alerts()

            assert response == mock_response
            mock_client.post.assert_called_once_with("/", json=payload)

    @patch("py_connect_test.services.http.httpx.Client")
    def test_post_alerts_uses_webhook_url(
        self,
        mock_client_class,
        http_test_instance,
        mock_response,
    ):
        payload = {"alert": "test"}

        mock_client = MagicMock()
        mock_client.post.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        with patch("builtins.open", mock_open(read_data=json.dumps(payload))):
            http_test_instance.post_alerts()

            mock_client_class.assert_called_once_with(
                base_url=http_test_instance.alert_settings.webhook_url,
                verify=True,
            )

    @patch("py_connect_test.services.http.httpx.Client")
    def test_post_alerts_logs_success(
        self,
        mock_client_class,
        http_test_instance,
        mock_response,
        mock_logger,
    ):
        payload = {"alert": "test"}

        mock_client = MagicMock()
        mock_client.post.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        with patch("builtins.open", mock_open(read_data=json.dumps(payload))):
            http_test_instance.post_alerts()

            mock_logger.success.assert_called_once()

    def test_post_alerts_raises_on_file_not_found(self, http_test_instance):
        with patch("builtins.open", side_effect=FileNotFoundError), pytest.raises(
            FileNotFoundError,
        ):
            http_test_instance.post_alerts()

    @patch("py_connect_test.services.http.httpx.Client")
    def test_post_alerts_raises_on_http_error(
        self,
        mock_client_class,
        http_test_instance,
    ):
        payload = {"alert": "test"}

        mock_client = MagicMock()
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Server Error",
            request=MagicMock(),
            response=mock_response,
        )
        mock_client.post.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client
        with patch(
            "builtins.open",
            mock_open(read_data=json.dumps(payload)),
        ), pytest.raises(httpx.HTTPStatusError):
            http_test_instance.post_alerts()
