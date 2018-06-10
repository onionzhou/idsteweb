#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from testcase.page.idsteLogin import IDsteWebLogin
from utils.config import Config
import time
class TestWebLogin(unittest.TestCase):
    url = Config().get('URL')
    @classmethod
    def setUpClass(cls):
        cls.page = IDsteWebLogin()
        cls.page.get(cls.url)
    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def tearDown(self):
        self.page.refresh()
        # self.page.err_message_disappear()

    def testLoginUserNull(self):
        self.page.login('', 'onion')
        self.assertEqual(u'请输入用户名',self.page.err_message(), msg=None)


    def testLoginUserError(self):
        self.page.login('onion*onion', 'onion')
        self.assertEqual('登录用户名或密码错误', self.page.err_message(), msg=None)

    def testLoginPasswdError(self):
        self.page.login('onion','onionpppp')
        self.assertEqual('登录用户名或密码错误',self.page.err_message(), msg=None)

    def testLoginPasswdNull(self):
        self.page.login('onion','')
        self.assertEqual(u'请输入密码',self.page.err_message() , msg=None)


    # def testLoginSucess(self):
    #     self.page.login('onion', 'onion')

if __name__ =='__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestWebLogin('testLoginUserNull'))
    suite.addTest(TestWebLogin('testLoginUserError'))
    suite.addTest(TestWebLogin('testLoginPasswdNull'))
    suite.addTest(TestWebLogin('testLoginPasswdError'))
    # suite.addTest(TestWebLogin('testLoginSucess'))
    unittest.TextTestRunner().run(suite)