import json
from http import HTTPStatus

import typer

from py_connect_test.services.http import HttpTest
from py_connect_test.setup_logger import setup_logger

app = typer.Typer(help="Http Connection Test")

logger = setup_logger()


@app.command()
def test(
    insecure: bool = typer.Option(
        False,
        "-i",
        "--insecure",
        help="Bypass Certificate Checking",
    ),
    alerts: bool = typer.Option(
        False,
        "-a",
        "--alerts",
        help="Send Alert to Webhook (WEBHOOK_URL env variable)",
    ),
):
    http_test = HttpTest(insecure=insecure)
    status_code = http_test.get_status_code()
    if status_code != HTTPStatus.OK:
        logger.error("Error: %s", {status_code})
        return
    logger.success("Success: %s", {status_code})

    if alerts:
        alert = http_test.post_alerts()
        logger.success(json.dumps(alert, indent=2))


if __name__ == "__main__":
    app()
