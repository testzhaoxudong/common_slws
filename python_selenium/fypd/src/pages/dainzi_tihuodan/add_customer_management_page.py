from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from python_selenium.fypd.src.common.common_code import CommonCode
class AddCustomerManagementPage(CommonCode):
    dianzi_tihuodan = By.XPATH,'//*[@id="root"]/div/section/div/aside/div/ul/li[4]'                 #电子提货单【4】
    cus_manag = By.XPATH,'//*[@id="/billOfLoading$Menu"]/li[1]/a'                       #客户管理
    add_button = By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/button[1]'

    creditCode = By.ID,'creditCode'         #客户税号
    custname = By.ID,'custname'             #客户名称
    forshort = By.ID,'forshort'             #客户简称
    busideptprin = By.ID,'busideptprin'     #客户联系人
    prinphone = By.ID,'prinphone'           #客户手机号
    addressName = By.ID,'addressName'       #客户地区
    click_addressName = By.XPATH,'//*[@class="ant-cascader-menu-item"]'
    addressDetail = By.ID,'addressDetail'   #客户详细地址
    pres_button = By.XPATH,'//*[@class="ant-btn ant-btn-primary"]'                                      #保存
    cancel_button = By.XPATH,'//*[@class="ant-btn ant-btn-default ant-btn-two-chinese-chars"]'          #返回
    assert_success_text = By.XPATH,'//*[text()="操作成功"]'                                             #新增成功断言

    #方法一：填写所有输入框并点击【保存】按钮
    def add_customer_management_save_oper(self,driver,creditCode_value,custname_value,forshort_value,busideptprin_value,
                                                prinphone_value,addressName_value,addressDetail_value):
        object = CommonCode()
        object.click(driver,self.dianzi_tihuodan)
        sleep(0.5)
        object.click(driver,self.cus_manag)
        sleep(0.5)
        # WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_all_elements_located((self.add_button))).click()
        object.click(driver,self.add_button)
        object.send_keys(driver, self.creditCode,creditCode_value)
        object.send_keys(driver, self.custname,custname_value)
        object.send_keys(driver, self.forshort,forshort_value)
        object.send_keys(driver, self.busideptprin,busideptprin_value)
        object.send_keys(driver, self.prinphone,prinphone_value)
        object.click(driver,self.addressName)
        object.send_keys(driver, self.addressName,addressName_value)

        object.click(driver,self.click_addressName)
        object.send_keys(driver, self.addressDetail,addressDetail_value)
        object.click(driver,self.pres_button)
    #方法二：填写所有输入框并点击【返回】按钮
    def add_customer_management_cancel_oper(self,driver,creditCode_value,custname_value,forshort_value,busideptprin_value,
                                                prinphone_value,addressName_value,addressDetail_value):
        object = CommonCode()
        object.click(driver, self.dianzi_tihuodan)
        object.click(driver, self.cus_manag)
        object.click(driver, self.add_button)
        object.send_keys(driver, self.creditCode,creditCode_value)
        object.send_keys(driver, self.custname,custname_value)
        object.send_keys(driver, self.forshort,forshort_value)
        object.send_keys(driver, self.busideptprin,busideptprin_value)
        object.send_keys(driver, self.prinphone,prinphone_value)
        object.send_keys(driver, self.addressName,addressName_value)
        object.send_keys(driver, self.addressDetail,addressDetail_value)
        object.click(driver,self.cancel_button)
    #获取添加成功断言文本
    def add_customer_management_success_text(self,driver):
        assert_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.assert_success_text))).text
        return assert_text