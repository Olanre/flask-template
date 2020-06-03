import logging
from logging.config import dictConfig

from  config import logging_config

def setup_logger():
	logging.config.dictConfig(logging_config)

setup_logger()
log = logging.getLogger('default')