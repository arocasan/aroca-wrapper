import logging
import os
import time
from datetime import datetime

# Create a logger
log = logging.getLogger(__name__)
today = datetime.now().strftime("%Y-%m-%d")


def config_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a file handler
    file_handler = logging.FileHandler(f"logs/{today}_aroca_wrapper.log")
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter(
        "[ %(asctime)s ]-[ %(process)d ]-[ %(levelname)s ]-[ %(message)s ]"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    log.addHandler(console_handler)
    log.addHandler(file_handler)
