#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import DRIVER_PATH
from testcase.common.page import Page
import time
class TestWebLogin(unittest.TestCase):
    url = 'https://192.168.1.113/'
    login_button =(By.CLASS_NAME, 'login-btn')
    input = (By.CLASS_NAME,'el-input__inner')
    def setUp(self):
        self.driver =Page()
        self.driver.get(self.url)
        #self.wait = WebDriverWait(self.driver, 4)
    def tearDown(self):
        self.driver.quit()
    def testLogin(self):
        self.driver.wait(4).until(lambda test: test.find_element(self.login_button))
        t =self.driver.find_elements(*self.input)
        t[0].send_keys('onion') #账号
        t[1].send_keys('onion') #密码
        self.driver.find_element(*self.login_button).click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()