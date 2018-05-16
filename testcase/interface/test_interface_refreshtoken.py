#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from utils.client import HttpClient
from testcase.common.common import headers

class TestiDsteInterfaceTokenRefresh(unittest.TestCase):
    def setUp(self):
        self.client = HttpClient(url='https://192.168.1.223/api/site/login')
    def tearDown(self):
        pass
    def test_token_refresh(self):
        payload = {'data': {'username': 'admin', 'password': 'admin'}}
        respone =self.client.send(json=payload,headers=headers).json()
        respone['data']['token']
        refresh = HttpClient(url="https://192.168.1.223/api/site/refresh?access_token="+ \
                                 respone['data']['token'])
        new_response = refresh.send(headers=headers).json()
        self.assertEqual(new_response['status'], 0)
        self.assertNotEqual(respone['data']['token'],new_response['data']['token'])

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestiDsteInterfaceTokenRefresh('test_token_refresh'))
    unittest.TextTestRunner(verbosity=1).run(suit)

