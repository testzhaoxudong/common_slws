import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from python_selenium.wlhy.src.common.General_method import GeneralMethod


class Add_Vehicle_Page(GeneralMethod):
    wlhy = (By.XPATH,'//*[text()="网络货运"]')
    wlhy_vehicle = (By.XPATH,'//*[@id="/network$Menu"]/li[8]/a')
    add_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
    vehicle_id = (By.XPATH,'//*[@placeholder="请输入车牌号"]')#-----车牌号
    driver_id = (By.XPATH,'//*[@placeholder = "请输入身份证号"]')#-----身份证号
    vehicle_colour = (By.ID,'extend1')#-----车辆颜色
    vehicle_colour_white = (By.XPATH,'//*[text()="白色"]')
    vehicle_type = (By.XPATH,'//*[@id="trucktypeName"]/div/div/ul/li/div/input')#-----车辆类型
    vehicle_user = (By.ID,"ksptExtend2")#-----所有人
    use_nature = (By.XPATH,'//*[@id="ksptExtend3"]')#-----使用性质
    fazhengjiguan = (By.XPATH,'//*[@id="ksptExtend4"]')#-----发证机关
    register_time = (By.XPATH,'//*[@id="registertime"]/div/input')#-----注册日期
    keys_register_time = (By.XPATH,"/html/body/div[5]/div/div/div/div/div[1]/div/input")
    certificate_time = (By.XPATH,'//*[@id="certificatetime"]/div/input')#-----发证日期
    keys_certificate_time = (By.XPATH,'/html/body/div[6]/div/div/div/div/div[1]/div/input')
    # 车辆能源类型
    anniu = (By.XPATH,'//*[@class="ant-radio ant-radio-checked"]')
    load_weight = (By.XPATH,'//*[@id = "approvedLoadWeight"]')#------核定载重量(吨)
    total_eight = (By.XPATH,'//*[@id="totalWeight"]')#---------总重量(吨)
    licence_id = (By.XPATH,'//*[@id="ksptExtend9"]')#-------道路经营许可证编号
    vehicle_shibie_id = (By.XPATH,'//*[@id="ksptExtend18"]')#---车辆识别编号
    vehicle_colour1 = (By.XPATH,'//*[@id="ksptExtend19"]')#-----车辆颜色
    vehicle_pictuer = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[23]/div[1]/div[2]/div/span/div/span/input')
    licence_pictuer_1 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[23]/div[2]/div[2]/div[1]/div/span/div/span/input')
    licence_pictuer_2 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[23]/div[2]/div[2]/div[2]/div/span/div/span/input')
    driving_license_id_1 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[24]/div[2]/div[1]/div/span/div/span/input')
    driving_license_id_2 = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div/div[2]/div/div[24]/div[2]/div[2]/div/span/div/span/input')
    tijiao_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/button[1]')
    def add_click(self,driver):
        object = GeneralMethod()
        object.click(driver,self.wlhy)
        time.sleep(0.2)
        object.click(driver, self.wlhy_vehicle)
        time.sleep(0.2)
        object.click(driver, self.add_button)
    def vehicle_info(self,driver,vehicle_id,driver_id,vehicle_type,vehicle_user,use_nature,fazhengjiguan,keys_register_time,keys_certificate_time,load_weight,total_eight,licence_id,vehicle_shibie_id,vehicle_colour1,vehicle_pictuer,licence_pictuer_1,licence_pictuer_2,driving_license_id_1,driving_license_id_2):
        object = GeneralMethod()
        object.send_keys(driver,self.vehicle_id,vehicle_id)
        object.send_keys(driver,self.driver_id,driver_id)
        object.click(driver,self.vehicle_colour)
        time.sleep(0.1)
        object.click(driver,self.vehicle_colour_white)
        time.sleep(0.1)
        object.send_keys(driver,self.vehicle_type,vehicle_type)
        time.sleep(0.2)
        # object.enter(driver,'//*[@id="trucktypeName"]')
        # driver.find_element_by_xpath('//*[@id="trucktypeName"]/div/div/ul/li/div/input').send_Keys(Keys.ENTER)
        object.enter(driver,'//*[@id="trucktypeName"]/div/div/ul/li/div/input')
        object.send_keys(driver,self.vehicle_user,vehicle_user)
        object.send_keys(driver,self.use_nature,use_nature)
        object.send_keys(driver,self.fazhengjiguan,fazhengjiguan)
        object.click(driver,self.register_time)
        object.send_keys(driver,self.keys_register_time,keys_register_time)
        object.click(driver,self.certificate_time)
        object.send_keys(driver,self.keys_certificate_time,keys_certificate_time)
        object.click(driver,self.anniu)
        object.send_keys(driver,self.load_weight,load_weight)
        object.send_keys(driver,self.total_eight,total_eight)
        object.send_keys(driver,self.licence_id,licence_id)
        object.send_keys(driver,self.vehicle_shibie_id,vehicle_shibie_id)
        object.send_keys(driver,self.vehicle_colour1,vehicle_colour1)
        object.send_keys(driver,self.vehicle_pictuer,vehicle_pictuer)
        object.send_keys(driver,self.licence_pictuer_1,licence_pictuer_1)
        object.send_keys(driver,self.licence_pictuer_2,licence_pictuer_2)
        object.send_keys(driver,self.driving_license_id_1,driving_license_id_1)
        object.send_keys(driver,self.driving_license_id_2,driving_license_id_2)
        time.sleep(1)
        object.click(driver,self.tijiao_button)
        # time.sleep(60)






