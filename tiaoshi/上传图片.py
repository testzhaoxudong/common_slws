import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.business.WLHY.dindan_business import DinDan_Business
from src.business.WLHY.login_business import LoginBusiness
from src.common.General_method import GeneralMethod

driver,wait = GeneralMethod().chushihua_driver("wlhy_url")
LoginBusiness().yuzhi_login(driver,3)
# DinDan_Business().xinzeng_click(driver)
GeneralMethod().click(driver,(By.XPATH,'//*[text()="网络货运"]'))
time.sleep(0.5)
GeneralMethod().click(driver,(By.XPATH,'//*[@id="/network$Menu"]/li[9]'))
GeneralMethod().click(driver,(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/button[1]'))
GeneralMethod().up_picture(driver,(By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[21]/div[1]/div[2]/div/span/div/span/input'),r"C:\Users\Administrator\Desktop\data\juzhen\common\file\hasagai.jpeg")
GeneralMethod().click(driver,(By.XPATH,'//*[text()="请选择车辆颜色"]'))
GeneralMethod().click(driver,(By.XPATH,'//*[text()="白色"]'))
GeneralMethod().send_keys(driver,(By.XPATH,'//*[@id="trucktypeName"]/div/div/ul/li/div/input'),"pt")
time.sleep(0.5)
# GeneralMethod().enter(driver,(By.XPATH,'//*[@id="trucktypeName"]/div/div/ul/li/div/input'))
# driver.find_element_by_xpath('//*[@id="trucktypeName"]/div/div/ul/li/div/input').send_keys(Keys.ENTER)
GeneralMethod().enter(driver,'//*[@id="trucktypeName"]/div/div/ul/li/div/input')
GeneralMethod().send_keys(driver,(By.XPATH,'//*[@placeholder="请选择注册日期"]'),"2021-11-02")
time.sleep(4)
GeneralMethod().click(driver,(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/button[1]'))
