import os
import unittest
from BeautifulReport import BeautifulReport
from selenium.webdriver.common.keys import Keys

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from python_selenium.fypd.src.common.get_test_info import GetTestInfo


class CommonCode:
    """通用方法一：初始化浏览器"""
    def init_driver(self,key):
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = GetTestInfo().get_test_config("slws_url.csv",key)
        driver.get(url)
        wait = WebDriverWait(driver,10,0.2)
        return driver,wait
    """通用方法二：输入框"""
    def send_keys(self,driver,element,value):
        element = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(( element )))
        element.send_keys(value)
    """通用方法三：点击"""
    def click(self,driver,element):
        element = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(( element )))
        element.click()
    """通用方法四：截图"""
    def get_screenshot(self,driver,describe):
        get_system_time = time.strftime("%Y%m%d%H%M%S")
        pictuer_name = get_system_time + describe + ".png"
        pictuer_path = os.path.join(os.path.dirname(__file__),"..","..","pictures",pictuer_name)
        driver.get_screenshot_as_file(pictuer_path)
    """通用方法无：元素定位"""
    def element(self,driver,element):
        WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((element)))
    """停用方法六：BeautifulReport测试报告"""

    def beautifulreport(self,testcase_path,pattern,report_patn,report_name_miaoshu,report__miaoshu):
        #pattern:要执行的用力名称(pattern="test*.py")
        # testcase_path = os.path.join(os.path.dirname(__file__), "..", "..", "test_case", "dianzi_tihuodan")
        taojian = unittest.defaultTestLoader.discover(testcase_path, pattern=pattern)
        # report_patn = os.path.join(os.path.dirname(__file__), "..", "..", "..", "report")
        get_time = time.strftime("%Y%m%d%H%M%S")
        repoer_name = get_time + report_name_miaoshu + ".html"
        BeautifulReport(taojian).report(report__miaoshu,filename=repoer_name, report_dir=report_patn)
    """通用方法七：回退（backspace）"""
    def backspace(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_Keys(Keys.BACK_SPACE)



if __name__ == '__main__':
    CommonCode().init_driver("pc_url")
