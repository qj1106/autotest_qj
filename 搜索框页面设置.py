# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re


# 百度搜索设置

class qj_17 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox ()
        self.driver.implicitly_wait (10)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test17(self):
        driver = self.driver
        driver.get (self.base_url)
        driver.find_element_by_link_text ("设置").click()
        try:
            search = driver.find_element_by_link_text ("设置").find_element_by_xpath ("//*[@id='wrapper']/div[6]/a[1]")
        except:
            driver.get_screenshot_as_file ("D:\\qj\\测试搜索页面.png")
            print (u"查找元素失败")
        ActionChains (driver).move_to_element (search).click ().perform()
        url = driver.current_url
        print(url)
        driver.find_element_by_id("s1_2").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
        time.sleep(5)
        # 获取网页告警信息
        alert = driver.switch_to_alert()
        print(alert.text ())
        print(alert)
        # 接送告警
        alert.accept()
        # 取消對話框
        # alert.dismiss ()
        # 輸入值
        # alert.send_keys("ww")
        driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element (by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert ()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert ()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept ()
            else:
                alert.dismiss ()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit ()
        self.assertEqual ([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main ()
