import logging

log_format = (
    "%(asctime)s - %(name)s - %(levelname)s - "
    "%(filename)s:%(lineno)d - %(message)s"
)

logging.basicConfig(
    level = logging.CRITICAL,
    format = log_format
)

logger = logging.getLogger("My First Disha Logger")
logger.info("This is an infor message like very basic")