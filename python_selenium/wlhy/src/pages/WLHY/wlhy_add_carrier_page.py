import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.wlhy.src.common.General_method import GeneralMethod


class AddCarrierPage(GeneralMethod):
    jcxx = (By.XPATH,'//*[text()="基础信息"]')#------基础信息
    carrier_admin = (By.XPATH,'//*[text()="承运商管理"]')#----承运商管理
    xinzeng_button = (By.XPATH,'//*[text()="新增"]')#----新增按钮

    carrier_name = (By.ID,'name')#----承运商名称
    login_name = (By.ID,'userAccount')#----登录用户名
    jiancheng = (By.ID,'shortname')#----简称
    code_element = (By.ID,'code')#----编码
    addr_element = (By.ID,'addr')#----地址
    contacts_element = (By.ID,'contacts')#----联系人
    contacts_phone = (By.ID,"phone")#----联系人手机
    tijiao_button = (By.XPATH,'//*[text()="提 交"]')

    assert_fail = (By.XPATH,' /html/body/div[2]/div/span/div/div/div')
    assert_success = (By.XPATH,'//*[text()="简称"]')

    def click_add_buttom(self,driver):
        object = GeneralMethod()
        object.click(driver,self.jcxx)
        time.sleep(0.2)
        object.double_click(driver,self.carrier_admin)
        time.sleep(0.2)
        object.double_click(driver,self.xinzeng_button)

    def send_keys_carrier(self,driver,carrier_name,login_name,jiancheng,code_element,addr_element,contacts_element,contacts_phone):
        object = GeneralMethod()
        object.send_keys(driver,self.carrier_name,carrier_name)
        object.send_keys(driver,self.login_name,login_name )
        object.send_keys(driver,self.jiancheng,jiancheng )
        object.send_keys(driver,self.code_element,code_element )
        object.send_keys(driver,self.addr_element,addr_element )
        object.send_keys(driver,self.contacts_element,contacts_element )
        object.send_keys(driver,self.contacts_phone,contacts_phone )
        object.double_click(driver,self.tijiao_button)
        time.sleep(0.2)

    def add_fail_assert(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.assert_fail))).text

    def add_success_assert(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.assert_success))).text