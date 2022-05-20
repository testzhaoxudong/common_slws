import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.common.General_method import GeneralMethod


class AddHzuserPage(GeneralMethod):
    jcxx = (By.XPATH,'//*[text()="基础信息"]')
    hz_admin = (By.XPATH,'//*[@id="/base$Menu"]/li[2]')
    add_hzuser_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[6]/td/div/a[4]')
    user_hz = (By.ID,'account')
    user_phone = (By.ID,'phone')
    user_name = (By.ID,'realName')
    user_pass = (By.ID,"password")
    add_button = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]')
    duanyan_text = (By.XPATH,'/div/div/div/span')
    def click_add_hzuser_page(self,driver):
        object = GeneralMethod()
        object.click(driver,self.jcxx)
        time.sleep(0.5)
        object.click(driver,self.hz_admin)
        time.sleep(0.5)
        object.click(driver,self.add_hzuser_button)

    def add_hzuser_page(self,driver,user_hz,user_phone,user_name,user_pass):
        object = GeneralMethod()
        time.sleep(2)
        object.send_keys(driver,self.user_hz,user_hz)
        object.send_keys(driver,self.user_phone,user_phone)
        object.send_keys(driver,self.user_name,user_name)
        object.send_keys(driver,self.user_pass,user_pass)
        object.click(driver,self.add_button)
    def get_duanyan_text(self,driver):
        text_1 = WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(  self.duanyan_text  )).text
        print(text_1)
        return text_1



