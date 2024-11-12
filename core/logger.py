import logging
import logging.handlers
from datetime import datetime
import os
import sys
from ..logs.config import LogLevel
# Create the log directory if it doesn't exist
log_dir = "proj/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define the log format
log_format = "[%(levelname)s:%(asctime)s:%(filename)s:%(lineno)d] %(message)s"
# Set the log level from the config.py file
log_level = getattr(logging, LogLevel.upper())

# Create a logger
logger = logging.getLogger()
logger.setLevel(log_level)

# Create a file handler with rotation by file size
file_handler = logging.handlers.RotatingFileHandler(
    os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
    maxBytes=4*1024*1024,  # 4 MB
    backupCount=1
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))

# Create a stream handler for standard output
stream_handler = logging.StreamHandler()
stream_handler.setLevel(log_level)
stream_handler.setFormatter(logging.Formatter(log_format))

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)