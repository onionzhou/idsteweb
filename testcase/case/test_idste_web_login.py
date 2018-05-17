#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from testcase.common.browser import Browser
from utils.config import Config,DRIVER_PATH,DATA_PATH
from utils import Log
from utils.fileOperation import ExcelRead

class TestLogin(unittest.TestCase):
    url = Config().get('URL')
    excelfile = DATA_PATH + '\\testdata.xlsx'
    def setUp(self):
        self.driver = Browser().get(self.url,maximize_window=False)
    def tearDown(self):
        self.driver.quit()
    def testLogin(self):
        datas = ExcelRead(self.excelfile).data
        pass

if __name__ == "__main__":
    #unittest.main()
    excelfile = DATA_PATH + '\\testdata.xlsx'
    print(excelfile)
    datas = ExcelRead(excelfile,title_line=True).data()
    for d in datas:
        print(d)
