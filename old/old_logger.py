

"""
import logging
import logging.handlers
from datetime import datetime
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#from logs.config import logfolder, loglevel 
from  config import  Loglevel

# Create the log folder if it does not exist
log_folder = 'proj/logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Set the log format
log_format = '[%(levelname)s:%(asctime)s:%(filename)s:%(lineno)d] %(message)s'
log_file_name = "log_%Y%m%d_%H%M%S.log"
# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.handlers.RotatingFileHandler(
    os.path.join(log_folder, log_file_name),
    maxBytes=4 * 1024 * 1024,  # 4 MB
    backupCount=10
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))
LogFolder = logging.INFO
# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LogFolder.info)
console_handler.setFormatter(logging.Formatter(log_format))

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
 """