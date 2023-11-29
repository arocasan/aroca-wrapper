import logging
import time
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.basicConfig(
    handlers=[
        logging.FileHandler(f"{today}_aroca_wrapper.log"),
        console_handler,
    ],
    format="[ %(asctime)s ]-[ %(process)d ]-[ %(levelname)s ]-[ %(message)s ]",
    level=logging.DEBUG,
)
