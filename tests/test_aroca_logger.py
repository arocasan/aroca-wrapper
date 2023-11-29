import logging
import os
from datetime import datetime

import pytest

from config.aroca_logger import config_logger, log, today


@pytest.fixture(autouse=True)
def setup():
    config_logger()


def test_logger_file_exists():
    log_file = f"{today}_aroca_wrapper.log"
    assert os.path.exists(log_file)


def test_logger_level():
    assert log.level == logging.DEBUG


def test_logger_format():
    if not log.handlers:
        log.addHandler(logging.StreamHandler())  # Add a handler if none exists

    log_format = log.handlers.pop().formatter._fmt
    expected_format = (
        "[ %(asctime)s ]-[ %(process)d ]-[ %(levelname)s ]-[ %(message)s ]"
    )
    assert log_format == expected_format


def test_logger_console_handler_level():
    console_handler = None
    for handler in log.handlers:
        if isinstance(handler, logging.StreamHandler):
            console_handler = handler
            break

    assert console_handler is not None
    assert console_handler.level == logging.INFO


def test_logger_file_handler_exists():
    handlers = [
        handler for handler in log.handlers if isinstance(handler, logging.FileHandler)
    ]
    assert handlers


def test_logger_file_handler_filename():
    handlers = [
        handler for handler in log.handlers if isinstance(handler, logging.FileHandler)
    ]
    assert handlers[0].baseFilename.endswith(f"{today}_aroca_wrapper.log")
