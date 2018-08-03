import logging
import  logging.handlers
import datetime
logger = logging.getLogger('mylogger')
logger.setLevel(logging,DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('')