#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import Config,DRIVER_PATH,DATA_PATH
from utils import Log
from utils.fileRead import ExcelRead

class TestLogin(unittest.TestCase):
    #url = 'https://cloud.idste.org/'
    url =Config().get('URL')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def testLogin(self):
        wait = WebDriverWait(self.driver, 4)  # 显示等待4s
        self.driver.maximize_window()
        time.sleep(1)
        # 读取excelfile test
        excelfile =  DATA_PATH +'/testdata.xlsx'
        filedata = ExcelRead(execlfile=excelfile,title_line=True).data()
        phone = int(filedata[0]['phone'])
        password = filedata[0]['password']
        name = filedata[0]['name']

        # driver.find_element_by_xpath("//input[@type='phone']").send_keys('13982004967')
        self.driver.find_element_by_class_name("el-input__inner").send_keys(phone)
        self.driver.find_element_by_class_name("login-btn").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'school-name').click()
        time.sleep(1)
        wait.until(lambda test: test.find_element(By.CLASS_NAME, 'el-input__inner'))
        # driver.find_element(By.CLASS_NAME,'el-input__inner').send_keys("onion")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        # driver.find_element(By.CLASS_NAME,'el-icon-back').click()
        self.driver.find_element(By.XPATH, "//i[@class='el-icon-back']").click()
        Log.logger.info('test test etst xxxxx fffuuc')



if __name__ == "__main__":
    unittest.main()

