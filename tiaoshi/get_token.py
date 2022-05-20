from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://119.3.36.78:93/#/user/login"
driver.get(url)
username = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"username")))
username.send_keys("15566644444")
password = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
password.send_keys("123456")
login = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]')))
login.click()
print(driver.current_url)