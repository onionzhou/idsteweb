#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#测试web 端远程修改设备配置用例
import unittest
from testcase.common.page import Page
from testcase.common.common import *
import time

class DevConfModification(unittest.TestCase):
    url = 'https://192.168.1.113/'
    dev_name = 'onion2onion'

    @classmethod
    def setUpClass(cls):
        cls.driver = Page()
        cls.driver.get(cls.url)
        cls.login(cls,'onion','onion')
        cls.chooseCtrl(cls,cls.dev_name)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def tearDown(self):
        pass

    def login(self, user, passwd):
        self.driver.wait(4).until(lambda test: test.find_element(*login_button))
        t = self.driver.find_elements(*input)
        t[0].send_keys(user)  # 账号
        t[1].send_keys(passwd)  # 密码
        self.driver.find_element(*login_button).click()

    def chooseCtrl(self,dev_name):
        dev_names = self.driver.find_elements(*all_dev_name)
        for i in range(len(dev_names)):
            if dev_names[i].text ==dev_name:
                time.sleep(1)
                dev_names[i].click()


    def test_xxx(self):
        print('1')
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()