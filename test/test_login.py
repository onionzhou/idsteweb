#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#6.0 web login
from selenium import webdriver
import time

def login():
    driver = webdriver.Chrome()
    driver.get("https://cloud.idste.org/")
    time.sleep(1)
    #driver.find_element_by_xpath("//input[@type='phone']").send_keys('13982004967')
    driver.find_element_by_class_name("el-input__inner").send_keys("13982004967")
    time.sleep(2)
   # driver.find_elements_by_css_selector("[type = 'button']")
    driver.find_element_by_class_name("login-btn").click()
   # driver.find_element_by_xpath("//button[@type='button']").click()
    #driver.find_element_by_link_text(u"登录").click()
    time.sleep(10)








if __name__ == '__main__':
    login()