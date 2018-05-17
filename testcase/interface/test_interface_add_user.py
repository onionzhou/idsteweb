#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from testcase.common.common import headers
from utils.client import HttpClient
add_user_payload={"data":{"user":{"User_ID":'',"User_Name":"zhou","New_Pass_Word":"z1zz",
                                  "User_Desc":"z1zz","User_Sn":'',"IcCard":'',"User_Type":1,"User_Expiry":'',"Priority":50,
                                  "Phone":"13982000018","IC_Status":0,"Dpm_Name":"zzz","usbKey":'',"privilege":817}},"timeout":10000}
class TestInterfaceAddUser(unittest.TestCase):
    def setUp(self):
        payload = {'data': {'username': 'admin', 'password': 'admin'}}
        response = HttpClient(url='https://192.168.1.223/api/site/login')\
            .send(headers=headers,json=payload).json()
        self.token=response['data']['token']
    def test_add_user(self):
        r =HttpClient(url="https://192.168.1.223/api/user/new?access_token="+ self.token).send(
            json=add_user_payload,headers=headers).json()
        self.assertEqual(r['status'], 0)
if __name__ =='__main__':
    unittest.main()