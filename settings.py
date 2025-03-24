import logging

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    green = "\x1b[32m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + "%(asctime)s - %(levelname)s" + reset +":\t %(message)s",
        logging.INFO: green + "%(levelname)s" + reset + ":\t %(message)s",
        logging.WARNING: grey + "%(asctime)s - %(levelname)s" + reset + ":\t %(message)s",
        logging.ERROR: grey + "%(asctime)s - %(levelname)s" + reset + ":\t %(message)s",
        logging.CRITICAL: grey + "%(asctime)s - %(levelname)s" + reset + ":\t %(message)s",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a custom console handler and set the formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(CustomFormatter())

# Add the handler to the logger
logger.addHandler(console_handler)
