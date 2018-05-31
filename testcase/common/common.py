#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Provide public class
'''
from selenium.webdriver.common.by import By
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
              "Accept": "application/json, text/plain, */*",
              'Content-Type': 'application/json;charset = UTF - 8'
          }

login_button =(By.CLASS_NAME, 'login-btn')
input = (By.CLASS_NAME,'el-input__inner')
all_dev_name =(By.CSS_SELECTOR, 'div.text-wrap :first-child')
#面板区域获取
panel_body =(By.CSS_SELECTOR, 'div.panel-content :nth-child(1)')
panel_item =(By.CSS_SELECTOR, 'div.ctrl-item')
#error element
#登陆界面的错误提示
login_error =(By.CSS_SELECTOR,'div.el-message')

# 修改配置
#修改配置  日志  删除 刷新
#you need find bt_group ,to find next(eg: bt_change_setting)
bt_group =(By.CSS_SELECTOR,'div.el-button-group')
bt_change_setting =(By.CSS_SELECTOR,'i.fa')
bt_logs=(By.CSS_SELECTOR,'i.el-icon-document')
bt_del=(By.CSS_SELECTOR,'i.el-icon-delete')
bt_refresh =By.CSS_SELECTOR,'i.el-icon-refresh'


#修改配置弹窗
# 系统 视频 音频 监控
tab_sys=(By.CSS_SELECTOR,'div#tab-sys')
tab_video=(By.CSS_SELECTOR,'div#tab-running')
tab_audio=(By.CSS_SELECTOR,'div#tab-vol')
tab_moni = (By.CSS_SELECTOR,'div#tab-moni')

#保存 取消
btn_save =(By.CSS_SELECTOR,'div.submit-btns :nth-child(1)')
btn_cancel =(By.CSS_SELECTOR,'div.submit-btns :nth-child(2)')

#设备名称 物理位置 音频延迟
dev_name = (By.CSS_SELECTOR,'input#devname')
Phy_location = (By.CSS_SELECTOR,'input#address')
brd_off_delay =(By.CSS_SELECTOR,'input#brd-turnoff-delay')

#系统配置pane-sys main
sys_config = (By.CSS_SELECTOR,'div.sys-conf')
#开机方式  use  find-elements()[0]
#分辨率  use  find-elements()[1]
select_choose =(By.CSS_SELECTOR,'div.el-select')
all_items=(By.CSS_SELECTOR,'li.el-select-dropdown__item')
#联动开关机
dev_link_parent = (By.CSS_SELECTOR,'div.sys-checkbox')
dev_link  =(By.CSS_SELECTOR,'label.el-checkbox')

#系统所有的checkbox
# 0 投影仪  1 电脑  2 麦克风 3 分辨率内置 4 hdmi 内置  5 视屏亮度增强
# use find_elements()
all_checkboxs =(By.CSS_SELECTOR, 'span.el-checkbox__inner')
#-----------------
copyright = (By.CSS_SELECTOR, 'div.copyright-info')