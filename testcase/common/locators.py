#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    '''登陆界面的定位器'''
    login_button = (By.CLASS_NAME, 'login-btn')
    input = (By.CLASS_NAME, 'el-input__inner')
    login_error = (By.CSS_SELECTOR, 'div.el-message')
class MainLocators(object):
    # 定位# 设备# 任务# 媒体 # 日志
    tab_device =(By.CSS_SELECTOR, 'ul.el-menu :nth-child(1)')
    tab_task =(By.CSS_SELECTOR, 'ul.el-menu :nth-child(2)')
    tab_media =(By.CSS_SELECTOR, 'ul.el-menu :nth-child(3)')
    tab_note= (By.CSS_SELECTOR, 'ul.el-menu :nth-child(4)')
class DevPageLocators(object):
    '''设备页面定位器'''
    all_dev_name = (By.CSS_SELECTOR, 'div.text-wrap :first-child')
    # 面板区域获取
    panel_body = (By.CSS_SELECTOR, 'div.panel-content :nth-child(1)')
    panel_item = (By.CSS_SELECTOR, 'div.ctrl-item')

class TaskPageLocators(object):
    ''' 任务页面定位器'''
    pass

class MediaPageLocators(object):
    '''媒体页面定位器'''
    pass

class LogPageLocators(object):
    '''日志页面定位器'''
    pass

class ManagementPageLocators(object):
    '''管理页面定位器'''
    pass