import os
import logging
import sys
from pathlib import Path

from dotenv import load_dotenv


def initialize_logger(logger_name=''):
    load_dotenv(Path('.env'))

    if not os.path.exists(os.getenv('LOG_FOLDER')):
        os.makedirs(os.getenv('LOG_FOLDER'))

    if not os.path.exists(os.getenv('LOG_FILE')):
        open(os.getenv('LOG_FILE'), 'w+').close()

    logging.basicConfig(filename=os.getenv('LOG_FILE'), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    return logger
