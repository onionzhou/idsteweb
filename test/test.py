#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from utils.config import DRIVER_PATH,REPORT_PATH
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
def writeTest():
    row0 = ['User_Desc', 'User_Sn', 'IcCard', 'User_Type', 'User_Expiry', 'Phone',
            'IC_Status', 'Dpm_Name', 'User_Name', 'New_Pass_Word', 'Priority',
            'privilege', 'usbkey','xxx'
            ]
    test ={}
    f = ExcelWrite('1.xls','sheet0',row0,str(2))
    f.write()
    f.save()
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
if __name__ =='__main__':
    writeTest()
    #modify_xls()

