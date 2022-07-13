import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.dp.src.common.get_test_info import Get_Test_Info


class Common:
    """输入"""
    def send_keys(self,driver,element,send_keys_value):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(( element ))).send_keys(send_keys_value)
    """点击"""
    def click(self,driver,element):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(( element ))).click()
    """获取文本内容"""
    def get_text(self,driver,element):
        data = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(( element ))).text
        return data
    """获取截图"""
    def get_screenshot(self,miaoshu,driver):
        get_time = time.strftime("%Y%m%d%H%M%S")
        pictuer_name = get_time+miaoshu+".png"
        picture_path = os.path.join(os.path.dirname(__file__),"..","..","pictures",pictuer_name)
        driver.get_screenshot_as_file(picture_path)
    """初始化浏览器"""
    def init_driver(self,file_name,key):
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = Get_Test_Info().get_test_config(file_name,key)
        driver.get(url)
        wait = WebDriverWait(driver,10,0.2)
        return driver,wait
    """双击"""
    def double_click(self,driver,element):
        element = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(( element )))
        ActionChains(driver).double_click(element).perform()