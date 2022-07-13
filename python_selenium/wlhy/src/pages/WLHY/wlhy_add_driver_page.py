import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.wlhy.src.common.General_method import GeneralMethod


class AddDriverPage(GeneralMethod):
    wlhy = (By.XPATH,'//*[text()="网络货运"]')
    wlhy_driver = (By.XPATH,'//*[text()="司机管理"]')
    add_button = (By.XPATH,'//*[text()="新增"]')

    driver_name = (By.ID,"name")#-----------------司机姓名
    driver_phone = (By.ID,"phone")#-----------------手机号
    driver_id = (By.ID,"jszh")#-------------------身份证号
    vehicle_type = (By.XPATH,'//*[@id="zjcxList"]')
    vehicle_type_A1 = (By.XPATH,'//*[text()="A1"]')
    fzjg = (By.ID,"fzjg")#------------------------发证机关
    cyzgz = (By.ID,"cyzgz")#------------------从业资格证号
    js_start_time = (By.ID,"text2")#----驾驶证有效开始日期
    send_js_start_time = (By.XPATH,'//*[@class="ant-calendar-input "]')
    sf_start_time = (By.ID,"text3")#----身份证有效开始日期
    send_sf_start_time = (By.XPATH,'//*[@class="ant-calendar-input "]')
    sf_end_time = (By.ID,"text4")#------身份证有效结束日期
    send_sf_end_time = (By.XPATH,'//*[@class="ant-calendar-input "]')
    js_end_time = (By.ID,"yxqz")#-------驾驶证有效结束日期
    send_js_end_time = (By.XPATH,'//*[@class="ant-calendar-input "]')
    #短期驾驶证
    js_duan = (By.XPATH,'//*[@id="text1"]/label[1]/span[1]/input')
    #长期驾驶证
    js_chang = (By.XPATH,'//*[@id="text1"]/label[2]/span[1]/input')
    #身份证图片
    sf_picture_1 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[12]/div[1]/div[2]/div[1]/div/span/div/span/input')
    sf_picture_2 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[12]/div[1]/div[2]/div[2]/div/span/div/span/input')
    #驾驶证图片
    js_picture_1 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[12]/div[2]/div[2]/div[1]/div/span/div/span/input')
    js_picture_2 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[12]/div[2]/div[2]/div[2]/div/span/div/span/input')
    #司机签名
    driver_name_picture = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[13]/div[2]/div/span/div/span/input')
    #从业资格证
    zg_picture = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[14]/div[2]/div/span/div/span/input')
    tijiao_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/button[2]/span')

    assert_success = (By.XPATH,'//*[text()="保存成功"]')
    assert_fail = (By.XPATH,'/html/body/div[2]/div/span/div/div/div/div[1]')

    def click_add_driver(self,driver):
        object = GeneralMethod()
        object.click(driver,self.wlhy)
        time.sleep(0.2)
        object.double_click(driver,self.wlhy_driver)
        time.sleep(0.2)
        object.double_click(driver,self.add_button)
    def send_keys_driver_data(self,driver,driver_name,driver_phone,driver_id,fzjg,cyzgz,js_start_time,sf_start_time,sf_end_time,js_end_time,sf_picture_1,sf_picture_2,js_picture_1,js_picture_2,driver_name_picture,zg_picture):
        object = GeneralMethod()
        object.send_keys(driver,self.driver_name,driver_name)
        object.send_keys(driver,self.driver_phone,driver_phone )
        object.send_keys(driver,self.driver_id,driver_id )
        object.click(driver,self.vehicle_type)
        time.sleep(0.2)
        object.click(driver,self.vehicle_type_A1)
        object.send_keys(driver,self.fzjg, fzjg)
        object.send_keys(driver,self.cyzgz, cyzgz)
        object.click(driver,self.js_start_time)
        object.send_keys(driver,self.send_js_start_time, js_start_time)
        object.click(driver,self.sf_start_time)
        time.sleep(0.5)
        object.send_keys(driver,self.send_sf_start_time,sf_start_time )
        object.click(driver, self.sf_end_time)
        time.sleep(0.5)
        object.send_keys(driver,self.send_sf_end_time,sf_end_time )
        object.click(driver,self.js_duan)
        object.click(driver, self.js_end_time)
        time.sleep(0.5)
        object.send_keys(driver,self.send_js_end_time, js_end_time)
        object.click(driver,self.js_duan)
        object.send_keys(driver,self.sf_picture_1, sf_picture_1)
        object.send_keys(driver,self.sf_picture_2,sf_picture_2 )
        object.send_keys(driver,self.js_picture_1,js_picture_1 )
        object.send_keys(driver,self.js_picture_2,js_picture_2 )
        object.send_keys(driver,self.driver_name_picture, driver_name_picture)
        object.send_keys(driver,self.zg_picture,zg_picture)
        time.sleep(2)
        object.double_click(driver,self.tijiao_button)
        time.sleep(1)
        # time.sleep(60)

    def get_assert_success_text(self,driver):
        a = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.assert_success))).text
        return a

    def get_assert_fail_text(self,driver):
        b = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.assert_fail))).text
        return b
