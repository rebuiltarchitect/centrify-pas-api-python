from os import path, remove
import logging


class BasicClass(object):
    def __init__(self):
        self.current_number = 0
 
    def increment_number(self):
        self.current_number += 1
        self.logger.warning('Incrementing number!')
        self.logger.info('Still incrementing number!!')
 
    def decrement_number(self):
        self.current_number -= 1
 
    def clear_number(self):
        self.current_number = 0
 
    def configure_logger(self):
        # If applicable, delete the existing log file as it is overwritten each time
        if path.isfile("gears_processing.log"):
            remove("gears_processing.log")
 
        # Create the Logger
        self.logger = logging.getLogger('basic_class')
        self.logger.setLevel(logging.DEBUG)
 
        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler('logs/basic_class.log')
        logger_handler.setLevel(logging.DEBUG)
 
        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
       # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)
 
        # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('Completed configure_logger()!')
