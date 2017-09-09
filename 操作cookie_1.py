# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time, os, re
import unittest, qj_20


class qj_19 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox ()
        self.base_url = 'https://www.baidu.com'
        self.driver.implicitly_wait (10)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test19(self):
        driver = self.driver
        driver.get (self.base_url)
        # # 添加 cookie 信息，字典
        # driver.add_cookie ({'name': 'TEST', 'value': 'test'})
        #
        # # driver.delete_cookie ('expiry')
        #
        # # 获得 cookie 信息
        # cookies = driver.get_cookies ()
        # for cookie in cookies:
        #     print ("%s --> %r --> %s" % (cookie['name'], cookie['value'], cookie['domain']))
        # # driver.delete_all_cookies ()
        # print (cookies)
        qj_20.cookie (self)
        qj_20.quit (self)
