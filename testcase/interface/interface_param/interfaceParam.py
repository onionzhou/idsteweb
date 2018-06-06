#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.fileOperation import ExcelRead
from utils.config import Config,DATA_PATH

class InterfaceURL(object):
    base_url = Config().get('URL')
    url_file = DATA_PATH + '\\urldata.xlsx'
    url_data = ExcelRead(url_file, title_line=True).data()
    login_url = base_url + url_data[0]['urllist']

class InterfaceData(object):
    payload ={}
    url_file = DATA_PATH + '\\userdata.xlsx'
    url_data = ExcelRead(url_file, title_line=True).data()
    payload['data'] =url_data[0]
    login_data = payload

if __name__ == '__main__':
   pass
