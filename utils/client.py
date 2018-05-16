#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from  requests import
import requests
from  utils.Log import logger
import urllib

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    pass


class HttpClient(object):
    '''
    >>>>> HTTPClient('http://www.xxx.com').send()
    <Response [200]>
    '''
    def __init__(self, url, method='POST', headers=None, cookies=None):
        self.url = url
        self.method = method.upper()
        self.session = requests.session()
        if self.method not in METHODS:
            raise UnSupportMethodException('Unsupport Method:{0} '.format(self.method))
        self.setHeaders(headers)
        self.setCookies(cookies)
        self.session.verify =False

    def setHeaders(self, headers):
        if headers:
            self.session.headers.update(headers)

    def setCookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(method=self.method,
                                        url=self.url,
                                        params=params,
                                        data=data,
                                        **kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0} {1}'.format(self.method, self.url))
        logger.debug('sucess: {0}\n{1}'.format(response, response.status_code))
        return response


class HttpClient4py3():
    '''
    this url request achieve by python3 urllib
    '''

    def __init__(self, url, headers=None):
        self.url = url
        if headers:
            self.headers = headers

    def send(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        return response


if __name__ == '__main__':
    '''
     import ssl
     ssl.match_hostname = lambda cert, hostname: True
     respone  =HttpClient4py3(url = 'https://192.168.1.223').send()
     print(respone.read())
 '''
    #import ssl

    #ssl._create_default_https_context = ssl._create_unverified_context
    #r =requests.get(url='https://192.168.1.223',verify=False)
    r = HttpClient(url='https://192.168.1.223/', method='GET').send()
    print(r.text)
    #print(respone.text)
