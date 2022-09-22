# creating a class for logging
import logging

class AppLoger():
    def __init__(self, logger_name='my_log', log_file='my_log.log', level=logging.DEBUG, log_format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'):
        self.logger_name = logger_name
        self.log_file = log_file
        self.level = level
        self.log_format = log_format

    def log_setup(self):
        self.handler = logging.FileHandler(self.log_file)  #adding log file to file handler
        self.handler.setFormatter(self.log_format)         # setting the format for the logger

        logger = logging.getLogger(self.logger_name)  #creating the main logger
        logger.setLevel(self.level)                   #setting the logger lavel
        logger.addHandler(self.handler)               # adding the logger to file handler

        return logger 
