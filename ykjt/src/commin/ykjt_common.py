import os
import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ykjt.src.commin.get_ykjt_test_info import GetYkjtTestInfo


class Common:
    #元素定位并写入
    def send_keys(self,driver,element,send_keys_value):
        WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located( element )).send_keys( send_keys_value )
    #元素定位并点击
    def click(self,driver,element):
        WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located( element )).click()
    #获取截图
    def get_picture(self,driver,miaoshu):
        get_time_strftime = time.strftime("%Y%m%d%H%M%S")
        picture_name = get_time_strftime + miaoshu + ".png"
        picture_path = os.path.join(os.path.dirname(__file__),"..","..","pictures",picture_name)
        driver.get_screenshot_as_file(picture_path)
    #浏览器初始化
    def chushihua_driver(self,file_name,key):
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = GetYkjtTestInfo().get_test_config(file_name,key)
        driver.get(url)
        wait = WebDriverWait(driver,10,0.2)
        return driver,wait
    # 获取文本
    def get_text(self,driver,element):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located( element )).text

    #连接数据库
    def connect_47_97_212_214(self,sql):
        db_info = GetYkjtTestInfo().get_test_database("47.97.212.214.csv")
        connect = pymysql.connect(  user=db_info["Username"],
                                    password=db_info["Passwd"],
                                    host=db_info["Host"],
                                    database=db_info["dbName"],
                                    port=int(db_info["Port"]),
                                    charset='utf8')
        youbiao = connect.cursor()
        youbiao.execute(sql)
        connect.commit()
        result = youbiao.fetchall()
        youbiao.close()
        connect.close()
        return result
if __name__ == '__main__':
    guoneng = Common().connect_47_97_212_214("SELECT * FROM base_alarm where id=1507190252058505217")
    print(type(guoneng))
    print(guoneng,end=" ")



















