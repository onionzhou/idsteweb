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
    bd_task_body=(By.CSS_SELECTOR, 'div.bd-task') #bd_task Body
    #任务名称
    task_name =(By.CSS_SELECTOR,'div.name-input')
    name_input =(By.CSS_SELECTOR,'input.el-input__inner')
    # 0 强制接收 1 静音 2 视频 3 随机 4 全选设备
    check_boxs =(By.CSS_SELECTOR,'span.el-checkbox__inner')
    #时间编辑
    date_editor =(By.CSS_SELECTOR,'div.el-date-editor')
    date_input =(By.CSS_SELECTOR,'input.el-input__inner')

    #添加媒体文件 0 和设置执行时间按钮组 1
    radio_group =(By.CSS_SELECTOR,'div.el-radio-group')
    radio_buttons =(By.CSS_SELECTOR,'label.el-radio-button')
    # -------------------------------------------------------------------------
    #媒体文件按钮组
    # 0 添加  1 删除 2 上移 3 下移
    media_btn_group =(By.CSS_SELECTOR,'div.table-btn-group')
    media_btns =(By.CSS_SELECTOR,'button.el-button')

    #添加媒体资源窗口
    # add_media_body = driver.find_elements(By.CSS_SELECTOR, 'div.el-dialog')[1]
    add_media_body =(By.CSS_SELECTOR,'By.CSS_SELECTOR,div.el-dialog')
    # 获取媒体文件列表
    #list
    dialog_body =(By.CSS_SELECTOR,'div.el-dialog__body')
    #媒体列表
    dialog_list =(By.CSS_SELECTOR,'By.CSS_SELECTOR,tr.el-table__row')
    #确认按钮
    media_btn_confim =(By.CSS_SELECTOR, 'button.el-button')
    #---------------------------------------------------------------------------
    #设置执行时间界面
    exe_time_body = (By.CSS_SELECTOR,'div.el-card__body')
    #执行时间添加按钮
    exe_time_btn = (By.CSS_SELECTOR, 'button.el-button')
    #-------------------------------
    exe_time_list = (By.CSS_SELECTOR,'tr.el-table__row')
    #时间调整
    exe_time_adjustment =(By.CSS_SELECTOR, 'input.el-input__inner')
    #正常 插播
    time_switch =(By.CSS_SELECTOR, 'div.el-switch')
    #播出日期
    play_date_all =(By.CSS_SELECTOR, 'div.checkout-box')
    play_date_body =(By.CSS_SELECTOR, 'div.el-checkbox-group')
    #周一到周日 list
    play_date_single=(By.CSS_SELECTOR,'label.weekday')
    #删除执行时间
    exe_time_del_btn =(By.CSS_SELECTOR,'button.el-button--danger')


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