# logging_module/log_script.py
import logging
from datetime import datetime
from .logger_setup import setup_logging
import argparse


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Logging Script')
    parser.add_argument('config_path', type=str, help='Path to the config.ini file')
    args = parser.parse_args()

    # Setup logging with the provided config path
    setup_logging(args.config_path)

    # Sample log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


if __name__ == '__main__':
    main()
