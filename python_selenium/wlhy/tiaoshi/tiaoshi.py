import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from src.common.General_method import GeneralMethod

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://119.3.36.78:93/#/user/login/"
driver.get(url)

username = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"username")))
username.send_keys("tester")
password = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"password")))
password.send_keys("123456")
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'[type="submit"]'))).click()
yewu = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[text()="网络货运"]')))
yewu.click()
time.sleep(0.5)
dindan = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="/network$Menu"]/li[1]/a')))
ActionChains(driver).double_click(dindan).perform()
time.sleep(0.5)
# GeneralMethod().double_click(driver,dindan)
xinzeng = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located( (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/button[1]')))
# xinzeng.click()
ActionChains(driver).double_click(xinzeng).perform()


element=WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="shipAddressRegionName"]')))
# lis = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[5]/div/div[1]/div[2]/div/span/span')))

element.send_keys("北京 / 北京市 / 东城区")
# element.find_element(By.PARTIAL_LINK_TEXT,u"甘肃省")




