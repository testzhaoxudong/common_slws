from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CsdnLoginPage():
    #使用F12定位用户名输入框
    username = By.XPATH,'//*[placeholder="手机号"]'
    #使用F12定位密码输入框
    password = By.XPATH,'//*[placeholder="6位数字验证码"]'
    def csdn_login_page(self,driver,username,password):
        #输入用户名
        keys_username = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.username)))
        keys_username.send_keys(username)
        # 输入验证码
        keys_password = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.password)))
        keys_password.send_keys("password")
