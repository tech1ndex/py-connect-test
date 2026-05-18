import sys

import loguru
from loguru import logger


def setup_logger() -> loguru.Logger:
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
        level="INFO",
    )
    return logger
