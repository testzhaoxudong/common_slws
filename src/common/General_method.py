import os
import time
import unittest
from BeautifulReport import BeautifulReport
import pymysql
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from src.common.get_test_file import GetTestInfo

class GeneralMethod():
    """通用方法一：输入框"""
    def send_keys(self,driver,element,send_value):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  element  ))).send_keys(send_value)
    """通用方法二：点击"""
    def click(self,driver,element):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  element  ))).click()
    """通用方法三：清空"""
    def clear(self,driver,element):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  element  ))).clear()
    """通用方法四：截图"""
    def get_picture(self,driver,miaoshu):
        get_time = time.strftime("%Y%m%d%H%M%S")
        picture_name = get_time + miaoshu + " .png"
        picture_path = os.path.join(os.path.dirname(__file__),"..","..","pictures",picture_name)
        driver.get_screenshot_as_file(picture_path)
    """通用方法五：初始化浏览器"""
    def chushihua_driver(self,URL):
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = GetTestInfo().get_test_info("url.csv")
        driver.get(url[URL])
        wait = WebDriverWait(driver,10,0.2)
        return driver,wait
    """通用方法六：连接数据库"""
    def connect_sql(self,sql):
        # 先获取数据库的配置信息
        db_info = GetTestInfo().get_test_info("db.csv")
        print(db_info)
        # 使用三方库pymysql链接数据库并赋值给connect
        connect = pymysql.connect(host=db_info["Host"], user=db_info["Username"], password=db_info["Passwd"],
                               database=db_info["dbName"], port=int(db_info["Port"]),charset='utf8')
        #获取游标
        youbiao = connect.cursor()
        # 在游标中执行sql语句
        youbiao.execute(sql)
        # 如果执行的sql语句是DML（insertupdate, delete)语句，会产生事务，必须要提交数据库的事务
        connect.commit()
        # 如果执行的sql语句是DQL（select）语句，那么查询结果必须要获取到。  从游标中获取查询结果
        result = youbiao.fetchall()
        # 关闭游标
        youbiao.close()
        #关闭数据库
        connect.close()
        #返回查询结果
        return result
    """通用方法七：切换框架"""
    def switch_frame(self,driver,kuangjia,wait_object):
        #如果frame是默认框架
        if kuangjia == "default":
            driver.switch_to.default_content()  # 切默认
        elif  kuangjia=="parent":
            driver.switch_to.parent_frame()  # 切上一级
        # 否则：
        else:
            # 切入到某一个框架
            wait_object.until(EC.frame_to_be_available_and_switch_to_it(kuangjia))
# --------------------------------------------鼠标事件--------------------------------------------------------
    """通用方法八：鼠标双击"""
    def double_click(self,driver,element):
        doubble_element = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  element  )))
        ActionChains(driver).double_click(doubble_element).perform()
    """通用方法九：鼠标悬浮"""
    def move_to_element(self,driver,element):
        move_to_element = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  element  )))
        ActionChains(driver).move_to_element(move_to_element).perform()
    """通用方法十：鼠标拖动"""
    def drag_and_drop(self,driver,drag_element,drop_element):
        drag_element = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  drag_element  )))
        drop_element = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  drop_element  )))
        ActionChains(driver).drag_and_drop(drag_element,drop_element).perform()
    """通用方法十一：鼠标右击"""
    def context_click(self,driver,element):
        context_element = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located((  element  )))
        ActionChains(driver).context_click(context_element).perform()


    """通用方法十二：BeautifulReport测试报告"""
    def Beautiful_Report(self,case_path,report_path,report_miaoshu):
        case_dir = os.path.join(os.path.dirname(__file__),case_path,"test_case")
        tao_jian = unittest.defaultTestLoader.discover(case_dir,pattern="*case.py")
        report = os.path.join(os.path.dirname(__file__),report_path,"reports")
        get_time = time.strftime("%Y%m%d%H%M%S")
        report_name = get_time + report_miaoshu + ".html"
        BeautifulReport(tao_jian).report(description="自动化测试报告",filename=report_name,report_dir=report)
#----------------------------------------------------------下拉框------------------------------------------------------------------------------------
    """通用方法十三：定位下拉框"""
    def select_index(self,driver,element,index_value):
        select = Select(WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  )))
        select.select_by_index(index_value)#——通过选项的顺序，第一个为 0
    def select_value(self,driver,element,value):
        select = Select(WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  )))
        select.select_by_value(value)#——通过value属性
    def select_text(self,driver,element,text_value):
        select = Select(WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  )))
        select.select_by_visible_text(text_value)# ——通过选项可见文本
        """
        同时，Select提供了四种方法取消选择：
        deselect_by_index(index)
        deselect_by_value(value)
        deselect_by_visible_text(text)
        deselect_all()
        """

    """通用方法十四：上传图片"""
    def up_picture(self,driver,element,picture_path):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  )).send_keys(picture_path)

    """通用方式十五：元素定位"""
    def selenium_element(self,driver,element):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  ))

# ----------------------------------------------------------------键盘事件-----------------------------------------------------------------------
    """通用方法十六：退格键"""
    def backspace(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_Keys(Keys.BACK_SPACE)
    """通用方法十七：contrl_a"""
    def contrl_a(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_Keys(Keys.CANCEL,"a")
    """通用方法十八：contrl_x"""
    def contrl_x(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_Keys(Keys.CANCEL,"x")
    """通用方法十九：contrl_c"""
    def contrl_c(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_Keys(Keys.CANCEL,"c")
    """通用方法二十：contrl_v"""
    def contrl_v(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_Keys(Keys.CANCEL,"v")
    """通用方法二十一：回车"""
    def enter(self,driver,element):
        driver.find_element_by_xpath(  element  ).send_keys(Keys.ENTER)

    """通用方法二十二：获取文本"""
    def get_text(self,driver,element):
        text_1 = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  )).text
        return text_1

    def element (driver,element):
        WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  element  ))




