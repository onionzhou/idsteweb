#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import DRIVER_PATH
from testcase.common.page import Page
from testcase.common.locators import LoginPageLocators
from utils.config import Config
class TestWebLogin(unittest.TestCase):
    url = Config().get('URL')
    @classmethod
    def setUpClass(cls):
        cls.driver = Page()
        cls.driver.get(cls.url)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        self.driver.wait(2).until_not(lambda test:test.find_element(*LoginPageLocators.login_error))

    def login(self,user,passwd):
        self.driver.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_button))
        t = self.driver.find_elements(*LoginPageLocators.input)
        t[0].clear()
        t[1].clear()
        t[0].send_keys(user)  # 账号
        t[1].send_keys(passwd)  # 密码
        self.driver.find_element(*LoginPageLocators.login_button).click()

    def testLoginUserNull(self):
        self.login('','onion')
        self.driver.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_error))
        err_message =self.driver.find_element(*LoginPageLocators.login_error).text
        self.assertEqual('请输入用户名',err_message,msg=None)

    def testLoginUserError(self):
        self.login('onion*onion', 'onion')
        self.driver.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_error))
        err_message = self.driver.find_element(*LoginPageLocators.login_error).text
        self.assertEqual(u'登录用户名或密码错误', err_message, msg=None)

    def testLoginPasswdError(self):
        self.login('onion', 'onionpppp')
        self.driver.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_error))
        err_message = self.driver.find_element(*LoginPageLocators.login_error).text
        self.assertEqual(u'登录用户名或密码错误', err_message, msg=None)

    def testLoginPasswdNull(self):
        self.login('onion', '')
        self.driver.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_error))
        err_message = self.driver.find_element(*LoginPageLocators.login_error).text
        self.assertEqual(u'请输入密码', err_message, msg=None)

    def testLoginSucess(self):
       self.login('onion','onion')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestWebLogin('testLoginUserNull'))
    suite.addTest(TestWebLogin('testLoginUserError'))
    suite.addTest(TestWebLogin('testLoginPasswdNull'))
    suite.addTest(TestWebLogin('testLoginPasswdError'))
    suite.addTest(TestWebLogin('testLoginSucess'))
    unittest.TextTestRunner().run(suite)