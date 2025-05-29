import logging

class MyCustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        # You can send this to a DB, remote API, etc.
        print("🔵 Custom handler received:", log_entry)

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = MyCustomHandler()
logger.addHandler(handler)

logger.info("This will go through the custom handler!")
