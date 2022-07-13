import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
wlhy = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[text()="网络货运"]')))
wlhy.click()
# ActionChains(driver).double_click(wlhy).perform()
# time.sleep(2)
wlhy_hy = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="/network$Menu"]/li[1]/a')))
ActionChains(driver).double_click(wlhy_hy).perform()
# wlhy_hy.click()
xinzeng = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[text()="新增"]')))
ActionChains(driver).double_click(xinzeng).perform()
fahuoren = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="ant-input ant-select-search__field"]')))
# fahuoren.click()
fahuoren.send_keys("发货人")
shouhuoren = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="receiverName"]/div/div/ul/li/div/input')))
shouhuoren.send_keys("收货人")
fahuoren_phone = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="shipperPhone"]')))
fahuoren_phone.send_keys(17860905132)
shouhuoren_phone = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="receiverPhone"]')))
shouhuoren_phone.send_keys(18615153791)
fahuodizhi = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="shipAddressRegionName"]')))
fahuodizhi.click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@title="北京"]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@title="北京市"]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@title="东城区"]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="receiveAddressRegionName"]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[6]/div/div[1]/div[2]/div/span/div/div/div/div/ul[1]/li[2]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[6]/div/div[1]/div[2]/div/span/div/div/div/div/ul[2]/li'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[6]/div/div[1]/div[2]/div/span/div/div/div/div/ul[3]/li[2]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="shipFullAddress"]'))).send_keys("北京市东城区景山街道北京市东城区应急指挥中心东城区社会服务管理中心")
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="receiveFullAddress"]'))).send_keys("天津市河东区上杭路街道金湾花园(东院)金湾花园东院")
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="materialTotalnum"]'))).send_keys(10)
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="price"]'))).send_keys(1)
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*//*[@id="materialTotalamount"]'))).send_keys(100)
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="materialName"]'))).send_keys("废铜烂铁")
# WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[text()="提 交"]'))).click()
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/button[1]'))).click()



time.sleep(3)
# driver.close()




