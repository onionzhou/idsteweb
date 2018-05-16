#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from utils.config import DRIVER_PATH,REPORT_PATH
import os
import requests
from utils.client import HttpClient
from testcase.common.common import headers
def test1():
    t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    tm = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(t)
    print(tm)

def test2():
    screen_name = 'xxxx'
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    screenshot_path = REPORT_PATH + '\screenshot_%s' % day
    screen_time = time.strftime('%H:%M:%S', time.localtime(time.time()))

    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    path = screenshot_path + '/%s_%s.png' %(screen_name, screen_time)
    print(path)

def tokenRefresh():
    payload = {'data':{'username':'admin','password':'admin'}}
    url = 'https://192.168.1.223/api/site/login'
    r = requests.post(url = url,verify =False,json=payload,headers=headers )
    d = r.json()
    print(d)
    xx =d['data']['token']
    print(d['data']['expire'])
    uu = "https://192.168.1.223/api/site/refresh?access_token=" + d['data']['token']
    print(uu)
    x = requests.get(url = "https://192.168.1.223/api/site/refresh?access_token="+ d['data']['token'],verify =False,headers=headers )
    print(x.json())
def  token_refresh():
    payload = {'data': {'username': 'admin', 'password': 'admin'}}
    client = HttpClient(url='https://192.168.1.223/api/site/login')
    r = client.send(json=payload,headers=headers).json()
    print(r['data']['token'])
    new_url ="https://192.168.1.223/api/site/refresh?access_token="+r['data']['token']
    print(new_url)
    rr =HttpClient(url=new_url).send(headers=headers).json()
    print(rr)
    print(rr['data']['token'])
def logout():
    client = HttpClient(url='https://192.168.1.223/api/site/logout')
    r = client.send(headers=headers).json()
    print(r['status'])

if __name__ =='__main__':
    logout()

