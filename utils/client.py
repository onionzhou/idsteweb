#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from  requests import
import requests
from  utils.Log import logger

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']

class UnSupportMethodException(Exception):
    pass

class HttpClient(object):
    '''
    >>>>> HTTPClient('http://www.xxx.com').send()
    <Response [200]>
    '''
    def __init__(self,url,method = 'GET',headers = None,cookies = None):
        self.url = url
        self.method =  method.upper()
        self.session =requests.session()
        if self.method not in METHODS:
            raise UnSupportMethodException('Unsupport Method:{0} '.format(self.method))
        self.setHeaders(headers)
        self.setCookies(cookies)

    def setHeaders(self,headers):
        if headers:
            self.session.headers.update(headers)
    def setCookies(self,cookies):
        if cookies:
            self.session.cookies.update(cookies)
    def send(self,params =None,data=None,**kwargs):
        response = self.session.request(method=self.method,
                                        url=self.url,
                                        params=params,
                                        data=data,
                                        **kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0} {1}'.format(self.method, self.url))
        logger.debug('sucess: {0}\n{1}'.format(response, response.status_code))
        return response

if __name__ == '__main__':
    respone = HttpClient(url = 'http://192.168.3.116/',method = 'GET').send()
    print(respone.text)