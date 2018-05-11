#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://docs.python.org/3.5/library/logging.html?highlight=logging#module-logging
import logging
from utils.config import LOG_PATH,Config
from logging.handlers import TimedRotatingFileHandler

'''
    from utils.Log import logger
    logger.info('xxxx  log ')
'''
class Logger():

    def __init__(self,log_name='iDstewebtest'):
        self.logger = logging.getLogger(log_name)
        logging.root.setLevel(logging.NOTSET)
        # first read config.yml if not use default
        c = Config().get('log')
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'iDstewebtest.log'#''
        self.backup_count = c.get('backup') if c and c.get('backup') else 5
        #log output level
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING' #'WARNING'
        self.file_output_level =c.get('file_level') if c and c.get('file_level') else 'DEBUG' #'DEBUG'
        FORMAT =c.get('pattern') if c and c.get('pattern') else \
        '%(asctime)s - %(name)s -%(levelname)s - %(message)s'
        self.formatter = logging.Formatter(FORMAT)


    def getLogger(self):
        '''logger add log '''
        if not self.logger.handlers:  # Avoid duplicate logs
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            # recreate a log file dayily ,keep up to 'back_count' ,
            #back_count default 5
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
