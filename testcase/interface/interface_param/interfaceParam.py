#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.fileOperation import ExcelRead
from utils.config import Config,DATA_PATH

def InterfaceURL():
    base_url = Config().get('URL')
    url_file = DATA_PATH + '\\urldata.xlsx'
    url_data = ExcelRead(url_file, title_line=True).data()
    login_url = base_url + url_data[0]['urllist']
    return login_url

def InterfaceData():

    payloadlist = []
    url_file = DATA_PATH + '\\userdata.xlsx'
    url_data = ExcelRead(url_file, title_line=True).data()

    for i in range(len(url_data)):
        payload = {}
        payload['data'] = url_data[i]
        # yield i
        payloadlist.append(payload)
    return payloadlist
    # print(payloadlist[0])
from utils.client import HttpClient
if __name__ == '__main__':
    # InterfaceData()
    url =InterfaceURL()
    # print(url)
    data = InterfaceData()
    print(data[0])
    c = HttpClient(url=url)
    for i in range(len(data)):
        res = c.send(params=data[i])
        print(res.text)
        print('--'*40)