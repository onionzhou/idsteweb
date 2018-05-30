#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.config import DRIVER_PATH
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
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
def case6():
    pass
    #操作面板开机关机
    # 用名字查找设备，名字需保持唯一
    # t = driver.find_elements(By.CSS_SELECTOR, 'div.text-wrap :first-child')
    # for i in range(len(t)):
    #     if t[i].text == 'onion2onion':
    #         time.sleep(1)
    #         t[i].click()  #选中onion2onion
    #-----------------------------------------------------
    #         get panle basic ctrl  |power on /off | prj open | pc open|forbidden
    #         panel_control[0-4] , 0 禁用 1 开机 2 关机 3.投影仪  4 电脑
            # panel_control = driver.find_element(By.CSS_SELECTOR, 'div.panel-content :nth-child(1)'). \
            #     find_elements(By.CSS_SELECTOR, 'div.ctrl-item')
    # panel_control[1].click()
    #-----------------------------------------------------------
    '''
               # brd button
                control=driver.find_element(By.CSS_SELECTOR,'div.panel-content').\
                    find_elements(By.CSS_SELECTOR,'div.panel-item')
                brd_control=control[1]
               # 广播按钮
               # brd_control.find_element(By.CSS_SELECTOR,'button').click()
                #音频控制
                # brd_control.find_element(By.CSS_SELECTOR,'div.volume-slider').\
                #     find_element(By.CSS_SELECTOR,'button').click()
                #音频滚动条拖动

                action = ActionChains(driver)
                bar = control[1].find_element(By.CSS_SELECTOR,'div.volume-slider').\
                    find_element(By.CSS_SELECTOR,'div.el-slider__button')
                action.drag_and_drop_by_offset(bar,100,00).perform()

                #麦克风控制
                #brd_control.find_element(By.CSS_SELECTOR, 'div.mic-slider').\
                    find_element(By.CSS_SELECTOR,'button').click()
                #麦克风滚动条控制
                mic_bar= control[1].find_element(By.CSS_SELECTOR,'div.mic-slider').\
                    find_element(By.CSS_SELECTOR,'div.el-slider__button')
                action.drag_and_drop_by_offset(mic_bar, 100, 00).perform()
                '''
def case7():
    pass
    #语言
    # driver.find_element(By.CSS_SELECTOR, 'button.lang-setting').click()
    # s = driver.find_elements(By.CSS_SELECTOR, "ul.el-dropdown-menu")[1].find_elements(By.CSS_SELECTOR, 'li')
    # for i in range(len(s)):
    #     print(s[i].text)
    #用户中心
    # driver.find_element(By.CSS_SELECTOR, 'button.user-info').click()
    # r = driver.find_elements(By.CSS_SELECTOR, "ul.el-dropdown-menu")[1].find_elements(By.CSS_SELECTOR, 'li')
    # for i in range(len(r)):
    #     print(r[i].text)
def test2():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    driver.get(url)
    wait = WebDriverWait(driver, 4, 0.5)
    wait.until(lambda test: test.find_element(By.CLASS_NAME, 'login-btn'))
    t = driver.find_elements(By.CLASS_NAME, 'el-input__inner')
    t[0].send_keys('')  # 账号
    t[1].send_keys('onion')  # 密码
    driver.find_element(By.CLASS_NAME, 'login-btn').click()
    wait.until(lambda test: test.find_element(By.CSS_SELECTOR,'div.el-message'))
    print(driver.find_element(By.CSS_SELECTOR,'div.el-message').text)

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
    driver.find_element(By.CSS_SELECTOR,'button.user-info').click()
    driver.find_elements(By.CSS_SELECTOR,"ul.el-dropdown-menu")[1].\
        find_elements(By.CSS_SELECTOR,'li')[0].click() #修改用户资料
    #add use info
    list =driver.find_element(By.CSS_SELECTOR,'form.userinfo-form :nth-child(3)').\
        find_element(By.CSS_SELECTOR,'div.el-input')
    print(list.text)
    time.sleep(4)
    #driver.quit()

def test3():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    driver.get(url)
    wait = WebDriverWait(driver, 4, 0.5)
    wait.until(lambda test: test.find_element(By.CLASS_NAME, 'login-btn'))
    t = driver.find_elements(By.CLASS_NAME, 'el-input__inner')
    t[0].send_keys('onion')  # 账号
    t[1].send_keys('onion')  # 密码
    driver.find_element(By.CLASS_NAME, 'login-btn').click()
    # -----------------------------------------------------------------
    # time.sleep(4)
    # 显示等待 两种形式
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.copyright-info')))
    wait.until(lambda test: test.find_element(By.CSS_SELECTOR, 'div.copyright-info'))

    t = driver.find_elements(By.CSS_SELECTOR, 'div.text-wrap :first-child')
    for i in range(len(t)):
        if t[i].text == 'onion2onion':
            time.sleep(1)
            t[i].click()  #选中onion2onion
    # 修改配置 (By.CSS_SELECTOR,'i.fa')
    # 日志 (By.CSS_SELECTOR,'i.el-icon-document')
    # 删除 (By.CSS_SELECTOR,'i.el-icon-delete')
    # 刷新 By.CSS_SELECTOR,'i.el-icon-refresh'
    driver.find_element(By.CSS_SELECTOR,'div.el-button-group').\
       find_element(By.CSS_SELECTOR,'i.fa').click()
    time.sleep(1)
    #修改配置 --
    # 系统 (By.CSS_SELECTOR,'div#tab-sys')
    #视频 (By.CSS_SELECTOR,'div#tab-running')
    # 音频 (By.CSS_SELECTOR,'div#tab-vol')
    # 监控 (By.CSS_SELECTOR,'div#tab-moni')
    #driver.find_element(By.CSS_SELECTOR,'div#tab-running').click()
    #-----------------------
    #系统修改配置
    # driver.find_element(By.CSS_SELECTOR,'input#devname').clear()#设备名称
    # driver.find_element(By.CSS_SELECTOR,'input#address').clear() #物理位置
    # driver.find_element(By.CSS_SELECTOR,'input#brd-turnoff-delay').clear()#音频输入延迟\
    # driver.find_element(By.CSS_SELECTOR, 'input#brd-turnoff-delay').send_keys('55')
    t =driver.find_elements(By.CSS_SELECTOR,'label.title')
    for i in range(len(t)):
        #print(t[i].text)
        if t[i].text == '开机方式':
            driver.find_element(By.CSS_SELECTOR,'div.el-input').click()






if __name__ =='__main__':
    test3()