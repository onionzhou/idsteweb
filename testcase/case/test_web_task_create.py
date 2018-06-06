#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from testcase.common.page import Page
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PATH,Config
from testcase.common.locators import LoginPageLocators,MainLocators,TaskPageLocators
import time

class TestTimeBrdTask(unittest.TestCase):
    url = Config().get('URL')

    @classmethod
    def setUpClass(cls):
        cls.driver = Page()
        cls.driver.get(cls.url)
        cls.login(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def login(self):
        # self.driver.get(self.url)
        self.driver.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_button))
        t = self.driver.find_elements(*LoginPageLocators.input)
        t[0].send_keys('admin')  # 账号
        t[1].send_keys('admin')  # 密码
        self.driver.find_element(*LoginPageLocators.login_button).click()
    def test_create_brd_task(self):
        time.sleep(1)
        self.driver.find_element(*MainLocators.tab_task).click()
        self.driver.find_element(*TaskPageLocators.el_main).\
            find_element(*TaskPageLocators.create_task).click()
        time.sleep(1)
        #任务名称
        brd_task =self.driver.find_element(*TaskPageLocators.brd_task)
        brd_task.find_element(*TaskPageLocators.task_name).\
            find_element(*TaskPageLocators.name_input).send_keys('音频广播')
        time.sleep(1)
        #时间表编辑
        brd_task.find_element(*TaskPageLocators.date_editor).click()

        edit_time =brd_task.find_element(*TaskPageLocators.date_editor).\
            find_element(*TaskPageLocators.date_input)
        edit_time.clear()
        edit_time.send_keys('010000')
        brd_task.click()
        time.sleep(1)
        #选中媒体添加
        brd_task.find_element(*TaskPageLocators.radio_group).\
            find_elements(*TaskPageLocators.radio_buttons)[0].click()
        #添加媒体
        time.sleep(1)
        # brd_task.find_element(*TaskPageLocators.media_btn_group).\
        #     find_elements(*TaskPageLocators.media_btns)[0].click()
        # time.sleep(4)
        self.driver.find_element(*TaskPageLocators.save_cancel_group).\
            find_elements(*TaskPageLocators.save_cancel_btns)[0].click()
        time.sleep(4)







class TestTimeControlTask(unittest.TestCase):
    pass

class TestManualControlTask(unittest.TestCase):
    pass

class TestManualBrdTask(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()