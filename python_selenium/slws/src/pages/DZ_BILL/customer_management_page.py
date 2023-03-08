from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.slws.src.common.slws_common import SLWS_COMMON


class CustomerManagementPage(SLWS_COMMON):
    dz_bill = (By.XPATH,'//div[@class="ant-menu-submenu-title"]')  #电子提货单[5]
    customer_management = (By.XPATH,'//li[@class="ant-menu-item ant-menu-item-selected"]')  #客户管理
    customer_management_add = (By.XPATH,'//*[text()="新增"]')    #新增按钮
    creditCode = (By.ID,"creditCode")        #客户税号
    custno = (By.ID,"custno")                #客户编码
    custname = (By.ID,"custname")            #客户名称
    forshort = (By.ID,"forshort")            #客户简称
    busideptprin = (By.ID,"busideptprin")    #客户联系人
    prinphone = (By.ID,"prinphone")          #客户手机号
    addressName = (By.ID,"addressName")      #客户地区
    addressDetail = (By.ID,"addressDetail")  #客户详细地址
    preserve_button = (By.XPATH,'//*[@class="ant-btn ant-btn-primary"]')  #保存按钮
    exit_button = (By.XPATH,'//*[@class="ant-btn ant-btn-default ant-btn-two-chinese-chars"]')  #返回按钮
    add_success_assert_element = (By.XPATH,'//*[text()="操作成功"]')
    add_fail_assert_element = (By.XPATH,"/html/body/div[3]/div/span/div/div/div/div[1]")
    def add_button(self,driver):
        SLWS_COMMON().click(driver,self.dz_bill)
        SLWS_COMMON().click(driver,self.customer_management)
        SLWS_COMMON().click(driver,self.customer_management_add)
    def customer_management_add_oper(self,driver,creditCode_value,custno_value,custname_value,forshort_value,
                                     busideptprin_value,prinphone_value,addressName_value,addressDetail_value):
        """所有参数全部填写并保存"""
        object = SLWS_COMMON()
        object.send_keys(driver,self.creditCode,creditCode_value)
        object.send_keys(driver,self.custno,custno_value)
        object.send_keys(driver,self.custname,custname_value)
        object.send_keys(driver,self.forshort,forshort_value)
        object.send_keys(driver,self.busideptprin,busideptprin_value)
        object.send_keys(driver,self.prinphone,prinphone_value)
        object.send_keys(driver,self.addressName,addressName_value)
        object.send_keys(driver,self.addressDetail,addressDetail_value)
        object.click(driver,self.preserve_button)
    def customer_management_required_add_oper(self,driver,creditCode_value,custno_value,custname_value,forshort_value):
        """所有必填信息全部填写并保存"""
        object = SLWS_COMMON()
        object.send_keys(driver,self.creditCode,creditCode_value)
        object.send_keys(driver,self.custno,custno_value)
        object.send_keys(driver,self.custname,custname_value)
        object.send_keys(driver,self.forshort,forshort_value)
        object.click(driver, self.preserve_button)
    def add_success_assert(self,driver):
        """获取新增成功断言文本"""
        assert_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(self.add_success_assert_element)).text
        return assert_text
    def add_fail_assert(self,driver):
        """获取新增失败断言文本"""
        assert_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(self.add_fail_assert_element)).text
        return assert_text
    def customer_management_add_exit_oper(self,driver,creditCode_value,custno_value,custname_value,forshort_value,
                                     busideptprin_value,prinphone_value,addressName_value,addressDetail_value):
        """所有参数全部填写并返回"""
        object = SLWS_COMMON()
        object.send_keys(driver,self.creditCode,creditCode_value)
        object.send_keys(driver,self.custno,custno_value)
        object.send_keys(driver,self.custname,custname_value)
        object.send_keys(driver,self.forshort,forshort_value)
        object.send_keys(driver,self.busideptprin,busideptprin_value)
        object.send_keys(driver,self.prinphone,prinphone_value)
        object.send_keys(driver,self.addressName,addressName_value)
        object.send_keys(driver,self.addressDetail,addressDetail_value)
        object.click(driver,self.exit_button)
