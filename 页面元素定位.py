# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re, os
import unittest
import HTMLTestRunner


class test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox ()
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search(self):
        driver = self.driver
        driver.get (self.base_url)
        driver.find_element_by_id ('kw').send_keys (u'测试')
        driver.find_element_by_id ('su').click ()
        time.sleep (2)
        driver.close ()

    def tearDown(self):
        self.driver.quit ()
        self.assertEqual ([], self.verificationErrors)


if __name__ == '__main__':
    # unittest.main ()
    suite = unittest.TestSuite
    suite.addTest (test ("test_search"))
    filename = "D:\\qj\\result.html"
    fp = open (filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner (stream=fp, title=u'测试报告', description=u'执行情况：')
    runner.run (suite)
