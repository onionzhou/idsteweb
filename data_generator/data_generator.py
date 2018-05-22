#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils import generator
from  utils.fileOperation import ExcelWrite
from utils.config import DATA_PATH

def increase_usr_data(filename,entry):
    '''用于生成用户数据，
     filename ：文件名  只支持 .xls结尾
     entry：生成数据条目
    '''
    title0 = ['User_Desc', 'User_Sn', 'IcCard', 'User_Type', 'User_Expiry', 'Phone',
            'IC_Status', 'Dpm_Name', 'User_Name', 'New_Pass_Word', 'Priority',
            'privilege', 'usbkey'
            ]
    user_data = []
    user_data.append(title0)
    #data generation
    for i in range(0,entry):
        list = []
        list.append(generator.random_name()) #姓名
        list.append(generator.rand_num(10)) #学工号
        list.append(generator.rand_num(10)) #卡号
        list.append(int(generator.rand_num_int(1,3))) #用户类型
        list.append(generator.random_date_generation())  #User_Expiry
        list.append(generator.random_phone_number()) #电话号码
        list.append(int(generator.rand_num_int(0,1))) # ic 卡状态
        list.append(generator.random_dpm_name()) #部门名称
        admin =generator.random_str(6,8).lower()
        list.append(admin)#登陆名 和密码
        list.append(admin)
        list.append(int(generator.rand_num_int(1,100))) #优先级
        list.append(int(generator.random_authority())) #privilege
        list.append(generator.random_usbkey())#usbkey
        user_data.append(list)

    #data wirte
    f = ExcelWrite(filename, 'sheet0')
    for  i in range(len(user_data)):
        for j in range(len(user_data[i])):
            f.write(i,j,user_data[i][j])
    f.save()

if __name__ == '__main__':
    filename = DATA_PATH + r'\userdata.xls'
    increase_usr_data(filename,20)#生成20条用户记录