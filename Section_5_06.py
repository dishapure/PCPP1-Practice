import logging
from colorlog import ColoredFormatter

# Set up a colored formatter
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s: %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

# Create handler and apply formatter
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Configure logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Example logs
logger.debug("Debugging info")
logger.info("General info")
logger.warning("Something unusual")
logger.error("Something went wrong")
logger.critical("System failure")
