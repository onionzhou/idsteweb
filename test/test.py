#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from utils.config import DRIVER_PATH,REPORT_PATH
import os
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
if __name__ =='__main__':
    print(time.localtime(time.time()))
    tm = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(tm)