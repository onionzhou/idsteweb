#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#send mail to tester
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

class Eamil():
    def __init__(self):
        '''
        :param title   主题
        :param memeage  正文
        :param from_addr  发件人地址
        :param to_addr    收件人地址
        :param sender    发件人
        :param Recipient 收件人  多个需要用分号'; '隔开
        :param server   smtp server
        '''
        pass
    def send(self):
        pass

