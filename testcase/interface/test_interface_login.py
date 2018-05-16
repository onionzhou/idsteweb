#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import unittest
from utils.client import HttpClient
import json

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
              "Accept": "application/json, text/plain, */*",
              'Content-Type': 'application/json;charset = UTF - 8'
          }
class TestiDsteInterfaceLogin(unittest.TestCase):
    def setUp(self):
        self.client = HttpClient(url='https://192.168.1.223/api/site/login')
    def tearDown(self):
        pass
    def test_normol_login(self):
        payload = {'data': {'username': 'admin', 'password': 'admin'}}
        r = self.client.send(headers=headers,json=payload)
        data = r.json()
        self.assertEqual(data['status'],0)
    def test_user_error_login(self):
        payload = {'data': {'username': 'xxxx', 'password': 'admin'}}
        r = self.client.send( headers=headers, json=payload)
        data = r.json()
        self.assertEqual(data['status'], 10002)
    def test_passwd_error_login(self):
        payload = {'data': {'username': 'admin', 'password': 'xxx'}}
        r = self.client.send( headers=headers, json=payload)
        data = r.json()
        self.assertEqual(data['status'], 10002)
    def test_null_user_login(self):
        payload = {'data': {'username': '', 'password': 'admin'}}
        r = self.client.send( headers=headers, json=payload)
        data = r.json()
        self.assertEqual(data['status'], 10002)
    def test_null_passwd_login(self):
        payload = {'data': {'username': 'admin', 'password': ''}}
        r = self.client.send( headers=headers, json=payload)
        data = r.json()
        self.assertEqual(data['status'], 10002)
    def test_all_null_login(self):
        payload = {'data': {'username': '', 'password': ''}}
        r = self.client.send(headers=headers, json=payload)
        data = r.json()
        self.assertEqual(data['status'], 10002)


class TestiDsteInterfaceLoginout(unittest.TestCase):
    def setUp(self):
        self.client =HttpClient(url = 'https://192.168.1.223/api/site/logout')

    def test_logout(self):
        #client = HttpClient(url='https://192.168.1.223/api/site/logout')
        data =self.client.send(headers=headers).json()
        self.assertEqual(data['status'], 0)


def test_main():
    '''
    单个用例添加
    '''
    suit = unittest.TestSuite()
    suit.addTest(TestiDsteInterfaceLogin('test_normol_login'))
    suit.addTest(TestiDsteInterfaceLoginout('test_logout'))
    unittest.TextTestRunner(verbosity=1).run(suit)

if __name__ =='__main__':
    #unittest.main()
    test_main()





