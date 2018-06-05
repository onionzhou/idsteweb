#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from testcase.case.test_web_login import *
from testcase.case.test_web_device_ctrl import *

def  test1():
    suite = unittest.TestSuite()
    # suite.addTest(TestWebDeviceCtrl('testOpenCtrl'))
    # suite.addTest(TestWebDeviceCtrl('testCloseCtrl'))
    # suite.addTest(TestWebLogin('testLoginUserNull'))
    suite.addTest(TestWebLogin('testLoginUserError'))
    suite.addTest(TestWebLogin('testLoginPasswdNull'))
    # suite.addTest(TestWebLogin('testLoginPasswdError'))
    # suite.addTest(TestWebLogin('testLoginSucess'))
    file = REPORT_PATH + '/report.html'
    with open(file, 'wb') as f:
        runner = HTMLTestRunner(f, title='idsteWebTestReport', verbosity=1,
                                description='HtmlTestRunner support py3')
        runner.run(suite)

if __name__ =='__main__':
    test1()