from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.business.WLHY.wlhy_add_hz_business import AddHzBusiness
from src.business.wlhy_add_hzuser_business import AddhzuserBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_hz_page import AddHzPage

# driver = GeneralMethod().chushihua_driver("wlhy_url")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://119.3.36.78:93/#/base/customer/add")
username = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"username")))
username.send_keys("wlhy_ptgn")
password = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
password.send_keys("123456")
login = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]')))
login.click()
# AddhzuserBusiness().add_hzuser_oper(driver,1)
AddHzBusiness().add_hz_oper(driver,1)
# AddHzPage().duanya_id_text(driver)
get_text = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[text()="提交成功"]'))).text
print(get_text)
# get_text_1 = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((By.XPATH,))).text
# print(get_text_1)

