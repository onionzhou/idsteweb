#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    '''登陆界面的定位器'''
    login_button = (By.CLASS_NAME, 'login-btn')
    input = (By.CLASS_NAME, 'el-input__inner')
    login_error = (By.CSS_SELECTOR, 'div.el-message')

class DevPageLocators(object):
    '''设备页面定位器'''
    pass

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