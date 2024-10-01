import os
import sys
import logging

# Define the format for logging messages, including timestamp, logging level, module name, and the message itself.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        # Write log messages to a file located at 'logs/running_logs.log'.
        logging.FileHandler(log_filepath),
        
        # Simultaneously print log messages to the standard output (console).
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a custom logger named "cnnClassifierLogger".
# This logger will use the settings defined above for capturing logs
logger = logging.getLogger("cnnClassifierLogger")