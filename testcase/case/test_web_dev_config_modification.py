#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#测试web 端远程修改设备配置用例
import unittest
from testcase.common.page import Page
from testcase.common.common import *
import time
from utils.config import Config

class DevConfModification(unittest.TestCase):
    url = Config().get('URL')
    dev_name = 'onion'

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
        time.sleep(1)
        # pass

    def login(self, user, passwd):
        self.driver.wait(4).until(lambda test: test.find_element(*login_button))
        t = self.driver.find_elements(*input)
        t[0].send_keys(user)  # 账号
        t[1].send_keys(passwd)  # 密码
        self.driver.find_element(*login_button).click()
        self.driver.wait(4).until(lambda test: test.find_element(*copyright))

    def chooseCtrl(self,dev_name):
        dev_names = self.driver.find_elements(*all_dev_name)
        for i in range(len(dev_names)):
            if dev_names[i].text ==dev_name:
                time.sleep(1)
                dev_names[i].click()
         #修改配置 ---> 系统
        self.driver.find_element(*bt_group).find_element(*bt_change_setting).click()
        self.driver.find_element(*tab_sys).click()

    def save(self):
        self.driver.find_element(*btn_save).click()
    def cancel(self):
        self.driver.find_element(*btn_cancel).click()
    #modify dev system config
    #testModifyDevSysConfig
    def testModifyDevName(self):
        self.driver.find_element(*dev_name).clear()
        self.driver.find_element(*dev_name).send_keys('tttttt')

    def testModifyPhyLocation(self):
        self.driver.find_element(*Phy_location).clear()
        self.driver.find_element(*Phy_location).send_keys('phylocationtest')

    def testBootModeChoose(self):
        #点击开机方式
        self.driver.find_element(*sys_config).find_elements(*select_choose)[0].click()
        #选择什么开机
        items= self.driver.find_elements(*all_items)
        for i in range(len(items)):
            if items[i].text == '面板':
                pass
            elif items[i].text == '插卡':
                items[i].click()
            elif items[i].text == '刷卡':
                pass
            elif items[i].text == '联动':
                pass
    def testLinkOpenMode(self):
        # 0 投影仪 1 电脑 2 麦克风
        self.driver.find_element(*dev_link_parent).\
            find_elements(*dev_link)[1].click()
    def testResolutionChoose(self):
        # x =self.driver.find_element(*sys_config).\
        #     find_elements(*all_checkboxs)[3]
        # x = self.driver.find_element(*sys_config). \
        #     find_elements(*all_checkboxs)[3]
        # if x:
        #     print('选中')
        # else:
        #     print('not ')

        self.driver.find_element(*sys_config).find_elements(*select_choose)[1].click()

        items = self.driver.find_elements(*all_items)
        for i in range(len(items)):
            if items[i].text == u'1366*768@60Hz':
                print('got it ')
                items[i].click()



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(DevConfModification('testResolutionChoose'))
    unittest.TextTestRunner().run(suite)