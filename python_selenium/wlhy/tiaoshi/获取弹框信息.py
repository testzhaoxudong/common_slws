import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.business.WLHY.login_business import LoginBusiness
from src.common.General_method import GeneralMethod

driver = webdriver.Chrome()
url = "http://119.3.36.78:93/#/user/login"
driver.get(url)
user = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="username"]')))
# user = driver.find_element_by_xpath('//*[@id="username"]')
user.send_keys('tester')
passwd = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
# passwd = driver.find_element_by_xpath('//*[@id="password"]')
passwd.send_keys("222222")
login_button = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]')))
login_button.click()
a = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/span/div/div/div/div[1]'))).text
time.sleep(1)
print(a.text)
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(1)
# alert.accept()


