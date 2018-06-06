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

    el_main =(By.CSS_SELECTOR,'main.el-main')
    #新建
    create_task =(By.CSS_SELECTOR,'div.el-button-group :nth-child(1)')
    #创建
    brd_task =(By.CSS_SELECTOR, 'div.bd-task')

    task_name =(By.CSS_SELECTOR,'div.name-input')
    name_input =(By.CSS_SELECTOR,'input.el-input__inner')
    # 0 强制接收 1 静音 2 视频 3 随机 4 全选设备
    check_boxs =(By.CSS_SELECTOR,'span.el-checkbox__inner')
    #时间编辑
    date_editor =(By.CSS_SELECTOR,'div.el-date-editor')
    date_input =(By.CSS_SELECTOR,'input.el-input__inner')
    #添加媒体文件和设置执行时间按钮组
    radio_group =(By.CSS_SELECTOR,'div.el-radio-group')
    radio_buttons =(By.CSS_SELECTOR,'label.el-radio-button')
    #媒体文件按钮组
    # 0 添加  1 删除 2 上移 3 下移
    media_btn_group =(By.CSS_SELECTOR,'div.table-btn-group')
    media_btns =(By.CSS_SELECTOR,'button.el-button')

    #save and cancel btn
    save_cancel_group=(By.CLASS_NAME,'footer')
    save_cancel_btns =(By.CSS_SELECTOR,'button.el-button')



class MediaPageLocators(object):
    '''媒体页面定位器'''
    pass

class LogPageLocators(object):
    '''日志页面定位器'''
    pass

class ManagementPageLocators(object):
    '''管理页面定位器'''
    pass