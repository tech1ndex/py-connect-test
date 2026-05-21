from __future__ import annotations

import sys

import typer

from py_connect_test.services.http import HttpTest
from py_connect_test.setup_logger import setup_logger

app = typer.Typer(help="Http Connection Test")

logger = setup_logger()


@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        sys.exit(0)


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
    logger.success("Connected: {}", status_code)

    if alerts:
        alert = http_test.post_alerts()
        logger.success("Alert response: {}", alert.status_code)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
