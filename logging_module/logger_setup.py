# logging_module/logger_setup.py
import logging
from datetime import datetime
import configparser
import os


def setup_logging(config_path):
    # Read configuration
    config = configparser.ConfigParser()
    config.read(config_path)

    # config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

    log_file_path = config['logging']['log_file_path']
    log_file_name = config['logging']['log_file_name']

    # Ensure the log file path exists
    if not os.path.exists(log_file_path):
        os.makedirs(log_file_path)

    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Generate the log file name with date
    full_log_file_name = f'{log_file_path}{log_file_name}_{current_date}.log'

    # Configure logging
    logging.basicConfig(
        filename=full_log_file_name,  # Log file name with current date
        filemode='a',  # Append mode
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        datefmt='%Y-%m-%d %H:%M:%S',  # Date format
        level=logging.DEBUG  # Log level
    )


# Ensure the setup_logging function can be imported without executing it immediately
if __name__ == '__main__':
    setup_logging()
