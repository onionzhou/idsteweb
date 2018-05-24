#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import DRIVER_PATH
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
url = "https://192.168.1.113/"
def case1():
    pass
    # 定位 设备 任务 媒体 日志
    # 1.driver.find_element(By.CSS_SELECTOR, 'ul.el-menu :nth-child(4)').click()
    # 2.driver.find_elements(By.CSS_SELECTOR, 'ul.el-menu')[0].\
    #     find_elements(By.CSS_SELECTOR,'li.el-menu-item')[2].click()
    # ------------------------------
def case2():
    pass
    # 定位
    # 修改配置 (By.CSS_SELECTOR,'i.fa')
    # 日志 (By.CSS_SELECTOR,'i.el-icon-document')
    # 删除 (By.CSS_SELECTOR,'i.el-icon-delete')
    # 刷新 By.CSS_SELECTOR,'i.el-icon-refresh'
    #driver.find_element(By.CSS_SELECTOR,'div.el-button-group').\
    #    find_element(By.CSS_SELECTOR,'i.el-icon-refresh').click()
    # ---------------------------------------------------------
def case3():
    pass
    #状态筛选
    #有时候出现元素没有点击到，需要加延时，以下为一个粗略的实现方法 或考虑execute_script

    # menu = driver.find_element(By.CSS_SELECTOR, 'span.el-input__suffix')
    # pc = driver.find_element(By.CSS_SELECTOR, 'ul.el-scrollbar__view :nth-child(1)')
    # prj = driver.find_element(By.CSS_SELECTOR, 'ul.el-select-dropdown__list :nth-child(2)')
    # brd = driver.find_element(By.CSS_SELECTOR, 'ul.el-select-dropdown__list :nth-child(3)')

    # 分步写 操作鼠标点击
    # action = ActionChains(driver)
    # action.move_to_element(menu).click().perform()
    #一起写
    # ActionChains(driver).move_to_element(menu).click().perform()

    # time.sleep(5)
    # ActionChains(driver).click(pc).click(prj).click(brd).perform()
    # time.sleep(5)
    # ActionChains(driver).click(pc).click(prj).click(brd).perform()
def case4():
    pass
    #check box 选择 r[0] 全选， r[1]第一个
    # r = driver.find_elements(By.CSS_SELECTOR, 'span.el-checkbox__inner')
    # r[2].click()

def case5():
    pass
    # 显示等待 两种形式
    # wait = WebDriverWait(driver, 4)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.copyright-info')))
    # wait.until(lambda test: test.find_element(By.CSS_SELECTOR, 'div.copyright-info'))
def test1():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
    driver.get(url)
    wait = WebDriverWait(driver,4,0.5)
    wait.until(lambda test: test.find_element(By.CLASS_NAME, 'login-btn'))
    t = driver.find_elements(By.CLASS_NAME, 'el-input__inner')
    t[0].send_keys('onion')  # 账号
    t[1].send_keys('onion')  # 密码
    driver.find_element(By.CLASS_NAME, 'login-btn').click()
    #-----------------------------------------------------------------
    #time.sleep(4)
    #显示等待 两种形式
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.copyright-info')))
    wait.until(lambda test: test.find_element(By.CSS_SELECTOR, 'div.copyright-info'))
    r =driver.find_elements(By.CSS_SELECTOR,'span.el-checkbox__inner')
    r[2].click()
    print(len(r))
    time.sleep(4)
    #driver.quit()
if __name__ =='__main__':
    test1()