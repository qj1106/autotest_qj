# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os


class qj_15 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox ()
        self.first_url = "https://www.baidu.com"
        self.second_url = "https://www.sogou.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 多个窗口切换，test方法要小写
    def test15(self):
        driver = self.driver
        # 百度页面-1
        driver.get (self.first_url + "/")
        # 通过js打开搜狗页面-2
        js1 = "window.open('https://www.sogou.com')"
        driver.execute_script (js1)
        # 通过js打开淘宝页面-2
        js2 = "window.open('https://www.taobao.com')"
        driver.execute_script (js2)

        # 获取当前窗口的句柄-百度（由于调用js打开新窗口）
        nowhandle = driver.current_window_handle
        nowurl = driver.current_url
        # 获取所有窗口的句柄集合
        allhandles = driver.window_handles
        print (allhandles)

        # 切换百度搜索
        for handle in allhandles:
            if handle == nowhandle:
                print ("切换窗口回:%r" % (nowurl))
                element = WebDriverWait (driver, 10).until (lambda driver: driver.find_element_by_id ("kw"))
                element.send_keys ("selenium")
                # driver.find_element_by_xpath("//*[@id='kw']").send_keys("auto测试")
                try:
                    driver.find_element_by_id ("ww").click ()
                    driver.get_screenshot_as_file ("D:\\qj\\测试搜索页面.png")
                    print (u"查找元素失败")
                except Exception as e:
                    print (Exception, ":", e)
                driver.find_element_by_id ("su").click ()

        time.sleep (5)
        driver.close ()

        # 切换回搜狗
        print (allhandles[1])
        driver.switch_to_window (allhandles[1])
        time.sleep (5)
        driver.find_element_by_id ('query').send_keys ("测试")
        driver.implicitly_wait (10)
        driver.close ()

        # 切换回淘宝
        print (allhandles[2])
        driver.switch_to_window (allhandles[2])
        # driver.quit ()


if __name__ == "__main__":
    unittest.main ()

# 多个窗口切换
# driver = webdriver.Firefox()

# 第一个页面
# first_url = driver.get("https://www.baidu.com")

# 第二个页面
# second_url = driver.get("https://www.sogou.com/")
# second_handle = driver.current_window_handle

# 新开一个窗口，通过执行js来新开一个窗口
# second_url = "https://www.sogou.com"
# js = 'window.open(second_url);'
# driver.execute_script(js)
# # 获取当前窗口的句柄
#
# # 当前窗口的句柄-百度
# nowhandle = driver.current_window_handle
#
# # 获取当前窗口句柄的集合
# allhandles = driver.window_handles
# print(allhandles)

# 切换窗口-百度
# for handle in allhandles:
#     if handle == nowhandle:
#         #
#         print("请切换页面",handle)
#         time.sleep(3)
#         driver.switch_to_window(handle)
#         # driver.find_element_by_xpath("//*[@id='query']").send_keys(u"auto测试")
#         driver.find_element_by_xpath("//*[@id='kw']").send_keys(u"auto测试")
#         try:
#             driver.find_element_by_id("ww").click()
#         except Exception as  e:
#             print(Exception,":",e)
#             driver.get_screenshot_as_file("D:\\qj\\测试搜索页面.png")
#             print(u"查找元素失败")
#         # driver.find_element_by_id("stb").click()
#         driver.find_element_by_id("su").click()
#
# time.sleep(5)
# driver.close()
#
# # 切换回搜狗
# print(allhandles[1])
# driver.switch_to_window(allhandles[1])
# driver.close()


# # 切换回第二个页面
# driver.switch_to_window(second_handle)
# try:
#     driver.find_elements_by_xpath("//*[@id='wrap']").send_keys("测试")
# except:
#     print(u"页面错误")
# driver.find_element_by_id("stb").click()
#
# time.sleep(3)
# driver.quit()
