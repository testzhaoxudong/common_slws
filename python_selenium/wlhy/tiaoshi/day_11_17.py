import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.business.WLHY.login_business import LoginBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_driver_page import AddDriverPage

# driver = GeneralMethod().chushihua_driver("wlhy_url")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://119.3.36.78:93/")
username = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"username")))
username.send_keys("wlhy_ptgn")
password = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
password.send_keys("123456")
login = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]')))
login.click()
AddDriverPage().click_add_driver(driver)
a = GeneralMethod().click(driver,(By.ID,"text2"))
# a.send_keys("2021-11-10")
time.sleep(2)
GeneralMethod().send_keys(driver,(By.XPATH,'//*[@class="ant-calendar-input "]'),"2021-11-10")