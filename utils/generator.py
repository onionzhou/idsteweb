#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from faker import Factory
import time
import datetime
'''
    random data generator
'''

fake = Factory.create('zh_CN')

def random_phone_number():
    """随机手机号"""
    return fake.phone_number()


def random_name():
    """随机姓名"""
    return fake.name()


def random_address():
    """随机地址"""
    return fake.address()


def random_email():
    """随机email"""
    return fake.email()


def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()


def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        # rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator

def random_num():
    return fake.random_digit()

def rand_num(max = 5):
    list =[]
    for i in range(0,max):
        list.append(str(random.randint(0,9)))
    return ''.join(list)

def rand_num_int(min=0,max=1):
    return random.randint(min,max)
def random_dpm_name():
    '''
      返回部门名称
    '''
    choice = ['组织部','人事处','档案部','科研处','财务处','学生处','科研处','保卫处']
    choice_gen =factory_choice_generator(choice)()
    return next(choice_gen)

def random_usbkey(max = 6):
    list =['3000']
    for i in range(0,max):
        list.append(str(random.randint(0,9)))
    return ''.join(list)

def random_authority():
    auth_data = [0,1, 16, 32, 256, 512]
    ##中控设备 1  #IC卡管理 16  #状态日志 32
    #音频广播 256  #ip呼叫权限 512  #物联设备控制 65536
    #x = random.randint(0,5)
    list =random.sample(auth_data,random.randint(0,5))
    if sum(list) == 0:
        return None
    else:
        return sum(list)

def random_date_generation():
    testnow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    time1 = (2018,1,1,0,0,0,0,0,0)
    time2 = (2018,12,31,23,59,59,0,0,0)
    start = time.mktime(time1)
    end = time.mktime(time2)
    #t  = random.randint(start,end)
    #date = time.localtime(t)
    #date1 =time.strftime('%Y-%m-%d %H:%M:%S',date)
    date = time.localtime(random.randint(start,end))
    return time.strftime('%Y-%m-%d %H:%M:%S',date)



def test():
    print(random_phone_number())
    print(random_name())
    print(random_address())
    print(random_email())
    print(random_ipv4())
    print(random_str(min_chars=6, max_chars=8))
    id_gen = factory_generate_ids(starting_id=0, increment=2)()
    for i in range(5):
        print(next(id_gen))
    choices = ['John', 'Sam', 'Lily', 'Rose']
    choice_gen = factory_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))


if __name__ == '__main__':
    random_date_generation()



