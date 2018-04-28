#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#6.0 web login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

def login():
    driver = webdriver.Chrome()
    driver.get("https://cloud.idste.org/")
    wait = WebDriverWait(driver,4) #显示等待4s
    driver.maximize_window()
    time.sleep(1)
    #driver.find_element_by_xpath("//input[@type='phone']").send_keys('13982004967')
    driver.find_element_by_class_name("el-input__inner").send_keys("13982004967")

    driver.find_element_by_class_name("login-btn").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,'school-name').click()
    time.sleep(1)
    wait.until(lambda test:test.find_element(By.CLASS_NAME,'el-input__inner'))
    #driver.find_element(By.CLASS_NAME,'el-input__inner').send_keys("onion")
    driver.find_element_by_xpath("//input[@type='password']").send_keys("onion")
    #driver.find_element(By.CLASS_NAME,'el-icon-back').click()
    driver.find_element(By.XPATH,"//i[@class='el-icon-back']").click()

if __name__ == '__main__':

    login()