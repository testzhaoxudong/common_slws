import os

import pymysql
from selenium.webdriver.common.keys import Keys

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
    """通用方法二十一：回车"""
    def enter(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_keys(Keys.ENTER)

    """连接数据库122.112.251.17"""
    def connect_db_122_112_251_17(self,sql):
        db_info = Get_Test_Info().get_test_database_config("db_122_112_251_17.csv",)
        connect = pymysql.connect(user=db_info["username"],
                                  password=db_info["password"],
                                  host=db_info["host"],
                                  database=db_info["database_name"],
                                  port=int(db_info["port"]) )
        #获取游标
        youbiao = connect.cursor()
        youbiao.execute(sql)
        connect.commit()
        res = youbiao.fetchall()
        youbiao.close()
        connect.close()
        return res
if __name__ == '__main__':
    res = Common().connect_db_122_112_251_17("SELECT * FROM `assayweight` WHERE id=10130020211214000458 AND varno=766")
    print(res)


