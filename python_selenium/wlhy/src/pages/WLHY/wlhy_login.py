from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from python_selenium.wlhy.src.common.General_method import GeneralMethod


class LoginPage(GeneralMethod):
    username_kuang = By.CSS_SELECTOR,'[id="username"]'
    password_kuang = By.CSS_SELECTOR,'[id="password"]'
    button = By.CSS_SELECTOR,'[class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]'
    login_abnormal_duanyan = By.XPATH,'/html/body/div[2]/div/span/div/div/div/div[1]'
    duanyan = By.XPATH,'//*[text()="首页"]'
    def login_oper(self,driver,username,password):
        GeneralMethod().send_keys(driver,self.username_kuang,username)
        GeneralMethod().send_keys(driver,self.password_kuang,password)
        GeneralMethod().click(driver,self.button)
    def login_success_assert(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.duanyan))).text

    def login_abnormal_assert(self,driver):
        assert_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.login_abnormal_duanyan))).text
        return assert_text
