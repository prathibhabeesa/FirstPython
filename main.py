import logging
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Generate the log file name
log_file_name = f'app_{current_date}.log'

# Configure logging
logging.basicConfig(
    filename=log_file_name,  # Log file name with current date
    filemode='a',  # Append mode
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
    level=logging.DEBUG  # Log level
)

# Sample log messages
logging.debug('This is a debug message1')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
