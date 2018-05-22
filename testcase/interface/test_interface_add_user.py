#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from testcase.common.common import headers
from utils.client import HttpClient
from utils.fileOperation import ExcelRead
from utils.config import DATA_PATH
import json
add_user_payload={"data":{"user":{"User_Name":"zho33333u1","New_Pass_Word":"z31zz",
                                  "User_Desc":"\u7f8a\u4e39","User_Sn":'',"IcCard":'',"User_Type":1,"User_Expiry":'',"Priority":50,
                                  "Phone":'13982000018',"IC_Status":1,"Dpm_Name":"\u79d1\u7814\u5904","usbKey":'',"privilege":817}},
                  "timeout":10000}
def getPayload():
    path = DATA_PATH + r'\userdata.xls'
    d = ExcelRead(path, title_line=True).data()
    #print(json.dumps({'data': {'user': d[0]}))
    return json.dumps({'data': {'user': d[0]}})

class TestInterfaceAddUser(unittest.TestCase):
    def setUp(self):
        payload = {'data': {'username': 'admin', 'password': 'admin'}}
        response = HttpClient(url='https://192.168.1.223/api/site/login')\
            .send(headers=headers,json=payload).json()
        self.token=response['data']['token']
    def test_add_user(self):
        payload =getPayload()
        print(payload)
        #print(add_user_payload)
        r =HttpClient(url="https://192.168.1.223/api/user/new?access_token="+ self.token).send(
            json=payload,headers=headers).json()
        self.assertEqual(r['status'], 0)
if __name__ =='__main__':
    unittest.main()
