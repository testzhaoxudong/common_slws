import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://test.fhf.dachebenteng.com/#/user/login/"
driver.get(url)
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("ykjt_slws_admin")
time.sleep(2)
password = driver.find_element_by_id("password")
password.send_keys("123456")
button = driver.find_element_by_xpath('//*[@type="submit"]')
button.click()
print(driver.get_cookies())