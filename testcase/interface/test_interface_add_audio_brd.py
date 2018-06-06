#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from utils.client import HttpClient
class TestInterfaceAddAudioBrd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = HttpClient(url='https://192.168.0.104/api/site/login')


    def setUp(self):
        pass

    def tearDown(self):
        pass