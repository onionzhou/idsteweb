#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import config,DRIVER_PATH

class TestLogin(unittest.TestCase):
    #url = 'https://cloud.idste.org/'
    url =config().get('URL')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def testLogin(self):
        wait = WebDriverWait(self.driver, 4)  # 显示等待4s
        self.driver.maximize_window()
        time.sleep(1)
        # driver.find_element_by_xpath("//input[@type='phone']").send_keys('13982004967')
        self.driver.find_element_by_class_name("el-input__inner").send_keys("13982004967")
        self.driver.find_element_by_class_name("login-btn").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'school-name').click()
        time.sleep(1)
        wait.until(lambda test: test.find_element(By.CLASS_NAME, 'el-input__inner'))
        # driver.find_element(By.CLASS_NAME,'el-input__inner').send_keys("onion")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("onion")
        # driver.find_element(By.CLASS_NAME,'el-icon-back').click()
        self.driver.find_element(By.XPATH, "//i[@class='el-icon-back']").click()


if __name__ == "__main__":
    unittest.main()

