#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from testcase.common.page import Page
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PATH,Config
from testcase.common.locators import LoginPageLocators,MainLocators,TaskPageLocators
from testcase.page.task import WebTask

import time

class TestTimeBrdTask(unittest.TestCase):
    url = Config().get('URL')
    @classmethod
    def setUpClass(cls):
        cls.page = WebTask()
        cls.page.get(cls.url)
        cls.page.login('onion','onion')
    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_create_brd_task(self):
        self.page.task_create()
        self.page.change_task_name('音频测试')
        self.page.add_exe_time('14:00:00')
        self.page.save_cancel_btn()
        time.sleep(3)

class TestTimeControlTask(unittest.TestCase):
    pass

class TestManualControlTask(unittest.TestCase):
    pass

class TestManualBrdTask(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()