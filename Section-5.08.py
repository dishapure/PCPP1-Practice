import logging
from logging.handlers import SMTPHandler

logger = logging.getLogger("emailLogger")
logger.setLevel(logging.ERROR)

mail_handler = SMTPHandler(
    mailhost=("smtp.gmail.com", 587),
    fromaddr="your_email@gmail.com",
    toaddrs=["dhruv.boston@gmail.com"],
    subject="URGENT ERROR",
    credentials=("your_email@gmail.com", "your_password!"),
    secure=()
)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
mail_handler.setFormatter(formatter)
logger.addHandler(mail_handler)

logger.error("Test error log via email.")
