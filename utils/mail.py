#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#send mail to tester
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import re

class Eamil():
    def __init__(self,server,
                 sender,s_password,
                 recipient,
                 title,message=None,annex=None):
        '''
        :param title   主题
        :param message  正文
        :param from_addr  发件人地址
        :param to_addr    收件人地址
        :param sender    发件人
        :param s_password  发件人密码
        :param Recipient 收件人  多个需要用分号'; '隔开
        :param server   smtp server
        :param annex   附件
        '''
        self.title = title
        self.message = message
        self.annex = annex
        self.sender = sender
        self.recipient = recipient
        self.s_password = s_password
        self.server= server
        self.msgRoot = MIMEMultipart('related') #related 可以包含
        # add annex in to email
    def _addAnnex(self,add_annex):
        att = MIMEText(open(add_annex,'rb').read(),'plain','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', add_annex)
        att["Content-Disposition"] = 'attachment; filename="%s" '%file_name[-1]


def send(self):
        pass

