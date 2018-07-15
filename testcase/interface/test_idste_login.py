#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from utils.config import REPORT_PATH
from utils.client import HttpClient
from utils.Log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode
from testcase.interface.interface_param.interfaceParam import *
# from testcase.interface.interface_param.interfaceParam import InterfaceData

class TestiDsteLogin(unittest.TestCase):
    url = InterfaceURL()
    data = InterfaceData()
    def setUp(self):
        self.client = HttpClient(url =self.url)
    def tearDown(self):
        pass
    def test_login_http(self):
        res = self.client.send(params=self.data[0])
        # logger.debug(res.text)
        self.assertEqual(200,res.status_code)
        # assertHTTPCode(res)
    def test_login_http_404(self):
        res = self.client.send(params=self.data[1])
        # logger.debug(res.text)
        self.assertEqual(200,res.status_code)
        # assertHTTPCode(res,404)

def test_main():
    report = REPORT_PATH + '\\interfacereport.html'
    suit = unittest.TestSuite()
    suit.addTest(TestiDsteLogin('test_login_http'))
    suit.addTest(TestiDsteLogin('test_login_http1'))

    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='idste interface login test',
                                description='interface html report')
        runner.run(suit)

if __name__ == '__main__':
    test_main()
