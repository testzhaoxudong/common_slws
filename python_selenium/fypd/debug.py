
#get_test_info
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.fypd.src.business.other.login_business import LoginBusiness
from python_selenium.fypd.src.common.common_code import CommonCode
from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.other.login_page import LoginPage

# if __name__ == '__main__':
# data = GetTestInfo().get_test_data("login_test_case_data.csv",1)
# print(data)
# config = GetTestInfo().get_test_config("url.csv","pc_url")
# print(config)
# driver = CommonCode().init_driver("pc_url")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://119.3.13.80:85/#/user/login')

# data =  GetTestInfo().get_test_data("login_test_case_data.csv",2)
# print(list(data))
# LoginBusiness().yuzhi_login_function(driver,1)
# LoginPage().login_oper(driver,data[0],data[1])
# username = By.ID,"username"  #用户名
# password = By.ID,"password"  #密码
login_button = By.XPATH, '//*[@class="ant-btn antd-pro-components-login-index-submit ant-btn-primary ant-btn-lg ant-btn-two-chinese-chars"]'
# object = CommonCode()
# 输入用户名
# object.send_keys(driver,username,'ykjt_slws_admin1')
# 输入密码
# object.send_keys(driver,password,'matrix@2022')
# 点击登录按钮
# object.click(driver,login_button)
username = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"username")))
username.send_keys('ykjt_slws_admin')
#
password = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.ID,"password")))
password.send_keys('matrix@2022')
#
WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((login_button))).click()

# a = driver.switch_to_alert()
# print(a.text)
# WebDriverWait(driver,10,0.2).until(expected_conditions.alert_is_present())  # 等待弹出窗口出现
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

# WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())  # 等待弹出窗口出现
# alert = driver.switch_to.alert
# 跳转倒alert
# alert = Alert(driver)
# print(alert.text)
# alert.accept()
# text_1 = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/span/div')))
# print(text_1.text)

# driver.quit()
#然后我们获取警告框，赋予变量名
# alert=driver.switch_to.alert
# 获取消息框文本在控制台打印
# print(alert.text)
# materialNo = GetTestInfo().get_test_data("add_tihuodan_management_test_data.csv",1)
# key = materialNo[0]
# print(key)
dianzi_tihuodan = By.XPATH, '//*[@id="root"]/div/section/div/aside/div/ul/li[4]'  # 电子提货单【4】
tihuodan_management = By.LINK_TEXT, '提货单管理'
# add_button = By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/button[1]'

materialNo = By.ID, "materialNo"
object = CommonCode()
object.click(driver,dianzi_tihuodan)
object.click(driver,tihuodan_management)
# sleep(2)
# object.click(driver,add_button)

object.click(driver,materialNo)
element = By.XPATH,'//ul[@role="listbox"]/li'
# text_1 = driver.find_elements_by_xpath('//ul[@role="listbox"]/li')
text_1 = WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_all_elements_located((element)))
# print(text_1.text)
for li in text_1:
    # print(text_1)
    print(li.text)
    if "粉煤（门克庆车队）" in li.text:
        li.click()

























