#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from utils.config import DRIVER_PATH,REPORT_PATH,DATA_PATH
import os
import requests
from utils.client import HttpClient
from testcase.common.common import headers
import xlrd
import xlwt
from xlutils.copy import copy
def test1():
    t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    tm = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(t)
    print(tm)

def test2():
    screen_name = 'xxxx'
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    screenshot_path = REPORT_PATH + '\screenshot_%s' % day
    screen_time = time.strftime('%H:%M:%S', time.localtime(time.time()))

    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    path = screenshot_path + '/%s_%s.png' %(screen_name, screen_time)
    print(path)

def tokenRefresh():
    payload = {'data':{'username':'admin','password':'admin'}}
    url = 'https://192.168.1.223/api/site/login'
    r = requests.post(url = url,verify =False,json=payload,headers=headers )
    d = r.json()
    print(d)
    xx =d['data']['token']
    print(d['data']['expire'])
    uu = "https://192.168.1.223/api/site/refresh?access_token=" + d['data']['token']
    print(uu)
    x = requests.get(url = "https://192.168.1.223/api/site/refresh?access_token="+ d['data']['token'],verify =False,headers=headers )
    print(x.json())
def  token_refresh():
    payload = {'data': {'username': 'admin', 'password': 'admin'}}
    client = HttpClient(url='https://192.168.1.223/api/site/login')
    r = client.send(json=payload,headers=headers).json()
    print(r['data']['token'])
    new_url ="https://192.168.1.223/api/site/refresh?access_token="+r['data']['token']
    print(new_url)
    rr =HttpClient(url=new_url).send(headers=headers).json()
    print(rr)
    print(rr['data']['token'])
def logout():
    client = HttpClient(url='https://192.168.1.223/api/site/logout')
    r = client.send(headers=headers).json()
    print(r['status'])
def get_server_info():
    client = HttpClient(url='https://192.168.1.223/api/site/stat')
    r = client.send(headers=headers).json()
    print(r)
def token_valid():
    client = HttpClient(url='https://192.168.1.223/api/site/login-valid',method='GET')
    r = client.send(headers=headers).json()
    print(r)


add_user_payload={"data":{"user":{"User_ID":'',"User_Name":"z1zz","New_Pass_Word":"z1zz",
                                  "User_Desc":"z1zz","User_Sn":'',"IcCard":'',"User_Type":1,"User_Expiry":'',"Priority":50,
                                  "Phone":"13982000018","IC_Status":0,"Dpm_Name":"zzz","usbKey":'',"privilege":817}},"timeout":10000}
def user_add():
    payload = {'data': {'username': 'admin', 'password': 'admin'}}
    client = HttpClient(url='https://192.168.1.223/api/site/login')
    r = client.send(json=payload, headers=headers).json()
    print(r['data']['token'])
    new_url = "https://192.168.1.223/api/user/new?access_token=" + r['data']['token']
    print(new_url)
    rr = HttpClient(url=new_url).send(headers=headers,json =add_user_payload).json()
    print(rr)
def xlsx_user_write():
    #e = 'F:\python\idsteweb\data\\randomuser.xlsx'
    f = xlwt.Workbook(encoding='utf-8') #创建工作薄
    '''create firsh sheet '''
    sheet1 = f.add_sheet('useradd',cell_overwrite_ok=True)
    sheet2 = f.add_sheet('useradd2', cell_overwrite_ok=True)
    sheet3 = f.add_sheet('useradd3', cell_overwrite_ok=True)
    row0 =['User_Desc','User_Sn','IcCard','User_Type','User_Expiry','Phone',
           'IC_Status','Dpm_Name','User_Name','New_Pass_Word','Priority',
           'privilege','usbkey',
           ]
    for i in range(0,len(row0)):
        #wirte(0,0,'xxx')   第1行 第1列 写入 xxx
       sheet1.write(0,i,row0[i])
    text = '王八'
    sheet1.write(1,0,text)
    f.save(r'demo.xls')
def xls_user_read():
    f = xlrd.open_workbook('demo.xls')
    print(f.sheet_names()) #获取表单名字
    f.sheet_by_index(1)
    f.sheet_by_name('useradd')


row0 = ['User_Desc', 'User_Sn', 'IcCard', 'User_Type', 'User_Expiry', 'Phone',
        'IC_Status', 'Dpm_Name', 'User_Name', 'New_Pass_Word', 'Priority',
        'privilege', 'usbkey', 'xxx'
        ]
def modify_xls():
    fr = xlrd.open_workbook('1.xls')
    fw = copy(fr)
    wb =fw.get_sheet('sheet0')
    for i in range(0,len(row0)):
        wb.write(0,i,row0[i])
    fw.save('1.xls')
from utils.fileOperation import ExcelWrite

def testxxxx():
    e= 'F:\python\idsteweb\data\\testdata.xlsx'
    file = xlrd.open_workbook(e)
    #file.sheet_by_index()
    sheetfile = file.sheet_by_name('Sheet1')
    title = sheetfile.row_values(0)
    data =[]
    for i in range(1,sheetfile.nrows):
        file =dict(zip(title,sheetfile.row_values(i)))
        data.append(file)
    print(data)

    '''for sheet in file.sheets():
        print(sheet.name)
    for i in range(sheetfile.nrows): #所有行 sheetfile.nrows
        row = sheetfile.row_values(i) # 打印每行的值
        print(row)
        for cell in row:
            print(cell) #打印每个表格的值
    print(sheetfile.row_values(0))
    '''
from utils import generator
def num_generator():
    print(generator.rand_num(10)) #学号
    print(generator.rand_num(10))  # 卡号
    print(generator.random_name())#姓名
    print(generator.random_str(6,8).lower()) #登陆名和密码
    print(generator.random_phone_number()) #电话号码
    print(generator.random_dpm_name()) #部门
    print(generator.rand_num()) #  IC卡状态 生成 0 1
    print(generator.rand_num(1,3)) #用户类型生成 123
    print(generator.rand_num(100)) #优先级  0 - 100
    print(generator.random_usbkey())#usbkey
     #授权管理


from utils.fileOperation import ExcelWrite


def random_user_add(filename,entry):
    title0 = ['User_Desc', 'User_Sn', 'IcCard', 'User_Type', 'User_Expiry', 'Phone',
            'IC_Status', 'Dpm_Name', 'User_Name', 'New_Pass_Word', 'Priority',
            'privilege', 'usbkey'
            ]
    user = []
    user.append(title0)
    #data generation
    for i in range(0,entry):
        list = []
        list.append(generator.random_name()) #姓名
        list.append(int(generator.rand_num(10))) #学工号
        list.append(int(generator.rand_num(10))) #卡号
        list.append(int(generator.rand_num_int(1,3))) #用户类型
        list.append(None)  #User_Expiry
        list.append(int(generator.random_phone_number())) #电话号码
        list.append(int(generator.rand_num_int(0,1))) # ic 卡状态
        list.append(generator.random_dpm_name()) #部门名称
        admin =generator.random_str(6,8).lower()
        list.append(admin)#登陆名 和密码
        list.append(admin)
        list.append(int(generator.rand_num_int(1,100))) #优先级
        list.append(None) #privilege
        list.append(int(generator.random_usbkey()))#usbkey
        user.append(list)

    #data wirte
    f = ExcelWrite(filename, 'sheet0')
    for  i in range(len(user)):
        for j in range(len(user[i])):
            f.write_test(i,j,user[i][j])
    f.save()
def bitOperation():
    print(1<<0)  #中控设备 1
    print(1 <<4) #IC卡管理 16
    print(1 << 5) #状态日志 32
    print(1 << 8) #音频广播 256
    print(1 << 9) #ip呼叫权限 512
    print(1 << 16) #物联设备控制 65536
from utils.fileOperation import ExcelRead
import json
def  readdata():
    path = DATA_PATH + r'\userdata.xls'
    d =ExcelRead(path,title_line=True).data()
    print(json.dumps({'data':{'user':d[0]}}))

def insert_task():
    for time in range(24):
        # "INSERT INTO `nccs`.`PlaySessionTime` (`SessionID`, `WeekDay`, `PlayTime`, `TempFlag`) VALUES ('2', '0', '2012-03-03 16:30:00', '0');
        print("insert into `nccs`.`PlaySessionTime` (`SessionID`, `WeekDay`, `PlayTime`, `TempFlag`) VALUES ('3', '0', '2012-03-03 %02d:30:00', '0');" % (time))
if __name__ =='__main__':
    readdata()
    #insert_task()

