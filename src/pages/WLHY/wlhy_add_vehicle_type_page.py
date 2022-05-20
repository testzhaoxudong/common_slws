import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.common.General_method import GeneralMethod


class AddVehicleTypePage(GeneralMethod):
    jcxx = (By.XPATH,'//*[text()="基础信息"]')#------基础信息
    vehicle_type = (By.XPATH,'//*[@id="/base$Menu"]/li[1]/a')#-----车辆类型
    add_button = (By.XPATH,'//*[text()="新增"]')#----新增

    vehicle_type_id = (By.XPATH,'//*[@placeholder="请输入车辆类型编码"]')#---------车辆类型编码
    vehicle_type_input = (By.ID,'vehicleType')#-----车辆类型
    tijiao_button = (By.XPATH,'//*[text()="提 交"]')
    success_assert = (By.XPATH, '//*[text()="提交成功"]')
    fail_assert = (By.XPATH,'//*[@class="ant-notification-notice-message"]')

    """点击进入新增车辆类型界面"""
    def click_add_button(self,driver):
        object = GeneralMethod()
        object.click(driver,self.jcxx)
        time.sleep(0.2)
        object.click(driver,self.vehicle_type)
        time.sleep(0.2)
        object.double_click(driver,self.add_button)
    """输入车辆类型并点击“提交”按钮  """
    def send_keys_vehicle_type(self,driver,vehicle_type_id,vehicle_type_input):
        object = GeneralMethod()
        object.send_keys(driver,self.vehicle_type_id,vehicle_type_id)
        object.send_keys(driver,self.vehicle_type_input,vehicle_type_input)
        object.double_click(driver,self.tijiao_button)

    """获取新增成功文本进行断言"""
    def add_success_assert(self,driver):
        text_1 = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located(self.success_assert)).text
        return text_1
    """获取新增失败文本进行断言"""
    def add_fail_assert(self,driver):
        text_1 = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located(self.fail_assert)).text
        return text_1