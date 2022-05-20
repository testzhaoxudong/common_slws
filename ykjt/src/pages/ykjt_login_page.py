from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ykjt.src.commin.ykjt_common import Common


class YkjtLoginPage(Common):
    username_kuang = (By.ID,"username")
    password_kuang = (By.ID,"password")
    quedin_button = (By.XPATH,'//*[@type="submit"]')
    assert_text = (By.XPATH,'//*[text()="已申请"]')
    fail_assert = (By.XPATH,'/html/body/div[2]/div/span/div/div/div')
    def ykjt_login(self,driver,username_value,password_value):
        object = Common()
        object.send_keys(driver,self.username_kuang,username_value)
        object.send_keys(driver,self.password_kuang,password_value)
        object.click(driver,self.quedin_button)

    def ykjt_yuzhi_login(self, driver, username_value, password_value):
        object = Common()
        object.send_keys(driver, self.username_kuang, username_value)
        object.send_keys(driver, self.password_kuang, password_value)
        object.click(driver, self.quedin_button)
    def login_success_assert(self,driver):
        # Common().get_text(driver,self.assert_text)
        text = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located(self.assert_text)).text
        # print(text)
        return text
    def login_fail_assert(self,driver):
        # Common().get_text(driver,self.fail_assert)
        text = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located(self.fail_assert)).text
        # print(text)
        return text