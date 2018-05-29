#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Provide public class
'''
from selenium.webdriver.common.by import By
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
              "Accept": "application/json, text/plain, */*",
              'Content-Type': 'application/json;charset = UTF - 8'
          }

login_button =(By.CLASS_NAME, 'login-btn')
input = (By.CLASS_NAME,'el-input__inner')
all_dev_name =(By.CSS_SELECTOR, 'div.text-wrap :first-child')
#面板区域获取
panel_body =(By.CSS_SELECTOR, 'div.panel-content :nth-child(1)')
panel_item =(By.CSS_SELECTOR, 'div.ctrl-item')
#error element
login_error =(By.CSS_SELECTOR,'div.el-message')