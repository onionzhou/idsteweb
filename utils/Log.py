#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from utils.config import LOG_PATH
from logging.handlers import TimedRotatingFileHandler

class Logger():

    def __init__(self,log_name='iDstewebtest'):
        self.logger = logging.getLogger(log_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'iDstewebtest.log'
        self.backup_count = 5
        #log output level
        self.console_output_level = 'WARNING'
        self.file_output_level ='DEBUG'
        FORMAT = '%(asctime)s - %(name)s -%(levelname)s - %(message)s'
        self.formatter = logging.Formatter(FORMAT)


    def getLogger(self):
        '''logger add log '''
        if not self.logger.handlers:  # Avoid duplicate logs
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            file_handler = TimedRotatingFileHandler(filename=LOG_PATH + self.log_file_name,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
            return self.logger


logger = Logger().getLogger()
