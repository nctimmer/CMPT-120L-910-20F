import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--reverse", help="This will reverse the order of the array", action="store_true")

import logging
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

logging.info("This is an info log message")
logging.warning("This is an warning log message")
logging.debug("This is an debug log message")
logging.error("This is an error log message")
logging.critical("This is an critical log message")