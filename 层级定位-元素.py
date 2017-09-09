# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class qj_16 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox ()
        self.driver.implicitly_wait (30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test16(self):
        driver = self.driver
        driver.get (self.base_url + "/")
        # CSS和XPATH定位
        # assert isinstance (driver.find_element_by_css_selector ("#u1 > a[name=\"tj_login\"]").click,object )
        # driver.find_element_by_css_selector ("#u1 > a[name=\"tj_login\"]").click ()
        # driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
        # driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__userName']").clear()
        # driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__userName']").send_keys ("test")
        # driver.find_element_by_css_selector("#TANGRAM__PSP_8__password").clear ()
        # driver.find_element_by_css_selector("#TANGRAM__PSP_8__password").send_keys ("www")

        # 其它方式-1-层级
        # driver.find_element_by_link_text ("登录").click ()
        # div = driver.find_element_by_id("TANGRAM__PSP_8__userNameWrapper").find_element_by_id ("TANGRAM__PSP_8__userName")
        # div.send_keys ("test")

        # 其它方式-2-层级
        # driver.find_element_by_id ("u1").find_element_by_class_name ("lb").click ()
        # div = driver.find_element_by_id("TANGRAM__PSP_8__form").find_element_by_id ("TANGRAM__PSP_8__userName")
        # div.send_keys("test")

        # driver.find_element_by_link_text ("登录").click ()
        # driver.find_element_by_class_name("tang-content").find_element_by_id ("TANGRAM__PSP_8__userName").send_keys("test")

        # 直接查
        driver.find_element_by_link_text ("登录").click ()
        driver.find_element_by_id ("TANGRAM__PSP_8__userName").send_keys ("test")
        driver.find_element_by_id ("TANGRAM__PSP_8__password").send_keys ("www")

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
