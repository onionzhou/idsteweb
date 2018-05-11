#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def assertHTTPCode(response,code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list=[200]
    if res_code not in code_list:
        raise AssertionError('status_code not in list ')