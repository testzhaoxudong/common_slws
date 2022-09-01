import os
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
        url = GetTestInfo().get_test_config("url.csv",key)
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
    """通用方法无：元素点位"""
    def element(self,driver,element):
        WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((element)))





if __name__ == '__main__':
    CommonCode().init_driver("pc_url")
