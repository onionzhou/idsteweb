#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from testcase.common.common import *
from testcase.common.page import Page
from selenium.webdriver.common.by import By
import time
class TestWebDeviceCtrl(unittest.TestCase):
    url = 'http://192.168.1.113/'
    @classmethod
    def setUpClass(cls):
        cls.driver = Page()
        cls.driver.get(cls.url)
        cls.login(cls)
    # def setUp(self):
    #     self.driver = Page()
    #     self.driver.get(self.url)
    #     self.Login()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def login(self):
        #self.driver.get(self.url)
        self.driver.wait(4).until(lambda test: test.find_element(*login_button))
        t = self.driver.find_elements(*input)
        t[0].send_keys('onion')  # 账号
        t[1].send_keys('onion')  # 密码
        self.driver.find_element(*login_button).click()
        #self.driver.wait(4).until(lambda test: test.find_element(By.CSS_SELECTOR, 'div.copyright-info'))
        self.ChooseCtrl(self)
    def ChooseCtrl(self):
        dev_names= self.driver.find_elements(*all_dev_name)
        for i in range(len(dev_names)):
            if dev_names[i].text == 'onion2onion':
                time.sleep(1)
                dev_names[i].click()
    def testOpenCtrl(self):
        # 0 禁用 1 开机 2 关机 3.投影仪  4 电脑
        panel_control = self.driver.find_element(*panel_body).\
            find_elements(*panel_item)
        panel_control[1].click()
    def testCloseCtrl(self):
        panel_control = self.driver.find_element(*panel_body). \
            find_elements(*panel_item)
        panel_control[2].click()


if __name__ =='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestWebDeviceCtrl('testOpenCtrl'))
    suite.addTest(TestWebDeviceCtrl('testCloseCtrl'))
    runner = unittest.TextTestRunner()
    runner.run(suite)