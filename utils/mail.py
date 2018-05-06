#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#send mail to tester
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from utils.Log import logger
import re

class Eamil():

    def __init__(self,server,
                 sender,s_password,
                 title,
                 recipient=None
                 ,message=None,annex=None):
        '''
        :param title   主题
        :param message  正文
        :param from_addr  发件人地址
        :param to_addr    收件人地址
        :param sender    发件人
        :param s_password  发件人密码
        :param Recipient 收件人
        :param server   smtp server
        :param annex   附件
        '''
        self.title = title
        self.message = message
        self.annexs = annex
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
        #print(file_name)
        #print(add_annex)
        att["Content-Disposition"] = 'attachment; filename="%s" '%file_name[-1]
        self.msgRoot.attach(att)
        logger.info('attach file {}'.format(add_annex))

    def send(self):
        COMMASPACE = ', '
        self.msgRoot['subject'] = self.title
        self.msgRoot['from'] = self.sender
       # self.msgRoot['to'] = self.recipient 单个字符串
        self.msgRoot['to'] =COMMASPACE.join(self.recipient)
        #添加正文
        if self.message :
            self.msgRoot.attach(MIMEText(self.message))
        #添加附件
        if self.annexs:
            if isinstance(self.annexs,str):
                self._addAnnex(self.annexs)
            elif isinstance(self.annexs,list):
                for file in self.annexs:
                    self._addAnnex(file)

        #link smtp server
        #s = smtplib.SMTP('smtp.qq.com')
        try:
            s =smtplib.SMTP(self.server)
        except:
            print('send fail can not connect smtp server ' )
        else:
            try:
                s.login(self.sender,self.s_password)
            except:
                print('login fail')
            else:
                s.sendmail(self.sender,self.recipient,self.msgRoot.as_string())
        finally:
            s.quit()


if __name__ == '__main__':
    '''
     1.支持附件上传
     2.支持多个用户接收
    '''
    file = 'F:\my_work\idsteweb\\report\\report.html'
    file1= 'F:\\1.png'
    e = Eamil(title='web test -.-ahhah',
              message='一波邮件测试',
              sender='寄件人',
              s_password='寄件人密码',
              #recipient=['xxxxxx@qq.com','xxxxx@foxmail.com'],
              recipient=['收件人'],
              annex=[file,file1],
              server='smtp.exmail.qq.com',
              )

    e.send()
