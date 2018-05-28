#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import DRIVER_PATH
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from testcase.common import browser
class Page(browser.Browser):
    def __init__(self):
        self.driver = super(Page,self).__init__()
    def find_element(self,*args):
        return self.driver.find_element(*args)
    def find_elements(self,*args):
        return self.driver.find_elements(*args)

import time
if __name__ == '__main__':
    driver = Page().get('https://192.168.1.113/')
    time.sleep(5)
    t=driver.find_elements(By.CLASS_NAME,'el-input__inner')
    t[0].send_keys('onion')  # 账号
    t[1].send_keys('onion')  # 密码
    driver.find_element(By.CLASS_NAME, 'login-btn').click()




