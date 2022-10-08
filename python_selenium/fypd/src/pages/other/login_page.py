from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.fypd.src.common.common_code import CommonCode
class LoginPage(CommonCode):
    username = By.ID,"username"  #用户名
    password = By.ID,"password"  #密码
    login_button = By.XPATH,'//*[@class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]'
    success_assert_text = By.XPATH,"//*[text()='兖矿能源石拉乌素厂区管理员']"  #登录成功断言文本
    fail_assert_text = By.XPATH,"/html/body/div[2]/div/span/div/div/div"       #登录失败断言文本


    def login_oper(self,driver,username_value,password_value):
        object = CommonCode()
        #输入用户名
        object.send_keys(driver,self.username,username_value)
        #输入密码
        object.send_keys(driver,self.password,password_value)
        #点击登录按钮
        object.click(driver,self.login_button)
    #登录成功断言方法
    def success_assert(self,driver):
        #获取登录成功断言文本
        text = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((self.success_assert_text))).text
        return text
        #登录成功断言方法
    def fail_assert(self,driver):
        #获取登录成功断言文本
        text = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((self.fail_assert_text))).text
        return text

