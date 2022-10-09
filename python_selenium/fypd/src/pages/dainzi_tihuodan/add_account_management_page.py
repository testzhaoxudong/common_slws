from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.common.by import By
from python_selenium.fypd.src.common.common_code import CommonCode


class AddAccountManagementPage(CommonCode):
    dianzi_tihuodan = By.XPATH, '//*[@id="root"]/div/section/div/aside/div/ul/li[4]'  # 电子提货单【4】
    account_management = By.LINK_TEXT,'账号管理'
    add_button = By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/button[1]'

    customer_name = By.XPATH,'//*[@class="ant-input ant-select-search__field"]'      #客户名称
    account = By.ID,'account'                                                        #用户账号
    realName = By.ID,'realName'                                                      #用户名称
    password = By.ID,'password'                                                      #用户密码

    save_button = By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/span/button'   #保存
    cancel_button = By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[5]/div[2]/div[1]/div/div/div/div[1]/div/div/button'      #返回

    success_text = By.XPATH,'//*[text()="操作成功"]'
    # exist_customer_account_management = By.XPATH,'//*[text()="该客户登录用户已存在！"]'      #该客户登录用户已存在
    # exist_account_management = By.XPATH,'//*[text()="该账号已被占用，不允许重复注册"]'       #该账号已被占用，不允许重复注册
    fail_text = By.XPATH,'/html/body/div[3]/div/span/div/div/div'

    def add_account_management_save_oper(self,driver,customer_name_value,account_value,realName_value,password_value):
        object = CommonCode()
        object.click(driver,self.dianzi_tihuodan)
        object.click(driver,self.account_management)
        sleep(1)
        object.click(driver,self.add_button)
        object.send_keys(driver,self.customer_name,customer_name_value)
        sleep(1)
        WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.customer_name))).send_keys(Keys.ENTER)
        object.send_keys(driver,self.account,account_value)
        object.send_keys(driver,self.realName,realName_value)
        object.send_keys(driver,self.password,password_value)
        object.click(driver,self.save_button)
        # alert = driver.switch_to.alert
        # print(alert.text)

    def add_account_management_cancel_oper(self,driver,customer_name_value,account_value,realName_value,password_value):
        object = CommonCode()
        object.click(driver,self.dianzi_tihuodan)
        object.click(driver,self.account_management)
        sleep(1)
        object.click(driver,self.add_button)
        object.send_keys(driver,self.customer_name,customer_name_value)
        object.send_keys(driver,self.account,account_value)
        object.send_keys(driver,self.realName,realName_value)
        object.send_keys(driver,self.password,password_value)
        object.click(driver,self.cancel_button)


    def add_account_management_success_text(self,driver):
        assert_text = WebDriverWait(driver,10,0.2).until(
            expected_conditions.presence_of_element_located((self.success_text))).text
        return assert_text

    def add_exist_customer_account_management_text(self,driver):
        exist_customer_account_management = WebDriverWait(driver,10,0.2).until(
            expected_conditions.presence_of_element_located((self.fail_text))).text
        return exist_customer_account_management

    # def add_exist_account_management_text(self,driver):
    #     exist_account_management_text = WebDriverWait(driver, 10, 0.2).until(
    #         expected_conditions.presence_of_element_located((self.fail_text))).text
    #     return exist_account_management_text