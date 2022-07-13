from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.dp.src.common.currency import Common


class Login_Page(Common):
    username = By.ID,"username"  #用户名
    password = By.ID,"password"  #密码
    login_button = By.XPATH,'//*[@type="submit"]' #登录按钮
    success_assert = By.XPATH,'//*[@class="antd-pro-components-global-header-index-name"]'
    fail_assert = By.XPATH,'//*[@class="ant-notification-notice-message"]'

    def loger_oper(self,driver,username_value,password_value):
        object = Common()
        object.send_keys(driver,self.username,username_value)
        object.send_keys(driver,self.password,password_value)
        object.click(driver,self.login_button)

    def get_login_success_assert_text(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(( self.success_assert ))).text

    def get_login_fail_assert_text(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(( self.fail_assert ))).text