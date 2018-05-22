#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import DRIVER_PATH
import time
class TestWebLogin(unittest.TestCase):
    url = 'https://192.168.1.223/'
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.url)
        #self.wait = WebDriverWait(self.driver, 4)
    def tearDown(self):
        self.driver.quit()
    def testLogin(self):
        #self.wait.until(lambda test: test.find_element(By.CLASS_NAME, 'el-input'))
        t =self.driver.find_elements(By.CLASS_NAME,'el-input__inner')
        t[0].send_keys('admin') #账号
        t[1].send_keys('admin') #密码
        self.driver.find_element(By.CLASS_NAME,'login-btn').click()

if __name__ == '__main__':
    unittest.main()