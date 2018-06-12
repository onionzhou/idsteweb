#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from testcase.common import browser
from testcase.common.locators import MainLocators,TaskPageLocators,LoginPageLocators
import time
from selenium.webdriver.common.keys import Keys
from testcase.page.idsteLogin import IDsteWebLogin

class WebTask(IDsteWebLogin,browser.Browser):
    def __init__(self,page=None,browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            self.driver = super().__init__(browser_type=browser_type)

    # def login(self, user, passwd):
    #     WebDriverWait(self.driver,2).until(lambda test: test.find_element(*LoginPageLocators.login_button))
        # self.wait(2).until(lambda test: test.find_element(*LoginPageLocators.login_button))
        # t = self.driver.find_elements(*LoginPageLocators.input)
        # t[0].clear()
        # t[1].clear()
        # t[0].send_keys(user)  # 账号
        # t[1].send_keys(passwd)  # 密码
        # self.driver.find_element(*LoginPageLocators.login_button).click()
        # time.sleep(1)
    def task_create(self):
        self.driver.find_element(*MainLocators.tab_task).click()
        self.driver.find_element(*TaskPageLocators.el_main).\
            find_element(*TaskPageLocators.create_task).click()
    def _brd_task_body(self):
        return self.driver.find_element(*TaskPageLocators.bd_task_body)

    def change_task_name(self,task_name):
        ctn =self.driver.find_element(*TaskPageLocators.bd_task_body).\
            find_element(*TaskPageLocators.task_name).\
            find_element(*TaskPageLocators.name_input)
        ctn.clear()
        ctn.send_keys(task_name)

    def brd_mute_click(self):
        #需判断check box 是否选中
        self._brd_task_body().find_elements(*TaskPageLocators.check_boxs)[0].click()
    def brd_video_click(self):
        self._brd_task_body().find_elements(*TaskPageLocators.check_boxs)[1].click()
    def random_play(self):
        self._brd_task_body().find_elements(*TaskPageLocators.check_boxs)[3].click()
    def check_all_devices(self):
        self._brd_task_body().find_elements(*TaskPageLocators.check_boxs)[4].click()
    def play_time_modification(self,time):
        self._brd_task_body().find_element(*TaskPageLocators.date_editor).click()
        edit_time =self._brd_task_body().find_element(*TaskPageLocators.date_editor).\
            find_element(*TaskPageLocators.date_input)
        edit_time.clear()
        edit_time.send_keys(time)
        self._brd_task_body().click()
    def add_brd_media_files(self,):
        self._brd_task_body().find_element(*TaskPageLocators.radio_group). \
            find_elements(*TaskPageLocators.radio_buttons)[0].click()
        self._brd_task_body().find_element(*TaskPageLocators.media_btn_group).\
            find_elements(*TaskPageLocators.media_btns)[0].click()
        add_media_body =self.driver.find_elements(*TaskPageLocators.add_media_body)[1]
        media_list =add_media_body.find_element(*TaskPageLocators.dialog_body).\
            find_elements(*TaskPageLocators.dialog_list)
        # 选中列表的第一个
        media_list[0].click()
        #确认
        add_media_body.find_element(*TaskPageLocators.media_btn_confim).click()

    def add_exe_time(self,task_time,index=0,mode=False):
        self._brd_task_body().find_element(*TaskPageLocators.radio_group). \
            find_elements(*TaskPageLocators.radio_buttons)[1].click()
        #执行时间添加按钮
        self._brd_task_body().find_element(*TaskPageLocators.exe_time_body).\
            find_element(*TaskPageLocators.exe_time_btn).click()
        time.sleep(1)
        time_list =self._brd_task_body().find_element(*TaskPageLocators.exe_time_body).\
            find_elements(*TaskPageLocators.exe_time_list)
        x =time_list[index].find_element(*TaskPageLocators.exe_time_adjustment)
        x.click()
        x.clear()
        x.send_keys(task_time)
        x.send_keys(Keys.ENTER)
        #是否插播
        if mode:
            time_list[index].find_element(*TaskPageLocators.time_switch).click()
        #全选
        time_list[index].find_element(*TaskPageLocators.play_date_all).click()
        #单选
        # weekday=time_list[index].find_element(*TaskPageLocators.play_date_body).\
        #     find_elements(*TaskPageLocators.play_date_single)
        # weekday[0].click()
        # weekday[1].click()

    def save_cancel_btn(self,bool=True):
        if bool:
            #确认
            self.driver.find_element(*TaskPageLocators.save_cancel_group).\
                find_elements(*TaskPageLocators.save_cancel_btns)[0].click()
        else:
            #取消
            self.driver.find_element(*TaskPageLocators.save_cancel_group). \
                find_elements(*TaskPageLocators.save_cancel_btns)[1].click()

