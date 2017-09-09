# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time


def quit(self):
    driver = self.driver
    driver.quit ()
    time.sleep (3)


def cookie(self):
    driver = self.driver
    # 添加cookie信息
    driver.add_cookie ({'name': 'TEST', 'value': 'test'})
    # 获得 cookie 信息
    cookies = driver.get_cookies ()
    for cookie in cookies:
        print ("%s --> %r --> %s" % (cookie['name'], cookie['value'], cookie['domain']))
    # 删除cookies--有问题
    # driver.delete_all_cookies ()
    print (cookies)
