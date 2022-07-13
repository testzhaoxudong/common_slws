import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.wlhy.src.common.General_method import GeneralMethod


class AddHzPage(GeneralMethod):
    jcxx = (By.XPATH,'//*[text()="基础信息"]')
    hz_admin = (By.XPATH,'//*[@id="/base$Menu"]/li[2]')#---------//*[@class="ant-menu-item ant-menu-item-selected"]
    xinzeng_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/button')
    hz_name = (By.XPATH,'//*[@placeholder="请输入货主名称"]')#-----货主名称
    credit_code = (By.XPATH,'//*[@id="creditCode"]')#-----统一社会信用代码
    login_name = (By.XPATH,'//*[@id="customerLoginAccount"]')#-----登录用户名
    hz_jianjie = (By.XPATH,'//*[@id="forshort"]')#-----货主简称
    yewu_leixing = (By.XPATH,'//*[@id="text6"]/div/div')#----业务类型
    yewu_leixing_1 = (By.XPATH,'//*[text()="干线普货运输"]')
    hangye = (By.XPATH,'//*[@id="industry"]')#-----行业
    hangye_1 = (By.XPATH,'//*[text()="煤炭"]')
    faren = (By.XPATH,'//*[@id="corp"]')#-----法人代表
    faren_id = (By.XPATH, '//*[@id="text4"]')#-----法人身份证号
    contacts = (By.XPATH,'//*[@id="busideptprin"]')#-----联系人
    contacts_phone = (By.XPATH,'//*[@id="prinphone"]')#-----联系电话
    ssxs = (By.XPATH,'//*[@id="text5"]')#-----所属销售
    bgdh = (By.XPATH,'//*[@id="phone"]')#-----办公电话
    beizhu = (By.XPATH,'//*[@id="remark"]')#-----备注
    faren_picture_1 = (By.XPATH,'//*[@id="text1"]')#-----法人身份证正面
    faren_picture_2 = (By.XPATH,'//*[@id="text2"]')#-----法人身份证反面
    khxk_picture = (By.XPATH,'//*[@id="text3"]')#-----开户许可证
    yyzz_picture = (By.XPATH,'//*[@id="licencecode"]')#-----营业执照
    tijiao_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/button[2]')
    duanyan_element = (By.XPATH,'/html/body/div[4]/div/span/div/div/div')
    success_duanya_text = ( By.XPATH,'//*[text()="提交成功"]')

    def xinzeng_click(self,driver):
        object = GeneralMethod()
        object.click(driver,self.jcxx)
        time.sleep(1)
        object.click(driver,self.hz_admin)
        time.sleep(0.2)
        object.click(driver,self.xinzeng_button)

    def send_keys_hz_data(self,driver,hz_name,credit_code,login_name,hz_jianjie,faren,faren_id,contacts,contacts_phone,ssxs,bgdh,beizhu,faren_picture_1,faren_picture_2,khxk_picture,yyzz_picture):
        object = GeneralMethod()
        object.send_keys(driver,self.hz_name,hz_name)
        object.send_keys(driver,self.credit_code,credit_code)
        object.send_keys(driver,self.login_name,login_name)
        object.send_keys(driver,self.hz_jianjie,hz_jianjie)
        object.click(driver,self.yewu_leixing)
        object.click(driver,self.yewu_leixing_1)
        object.click(driver,self.hangye)
        object.click(driver,self.hangye_1)
        object.send_keys(driver,self.faren,faren)
        object.send_keys(driver,self.faren_id,faren_id)
        object.send_keys(driver,self.contacts,contacts)
        object.send_keys(driver,self.contacts_phone,contacts_phone)
        object.send_keys(driver,self.ssxs,ssxs)
        object.send_keys(driver,self.bgdh,bgdh)
        object.send_keys(driver,self.beizhu,beizhu)
        object.send_keys(driver,self.faren_picture_1,faren_picture_1)
        object.send_keys(driver,self.faren_picture_2,faren_picture_2)
        object.send_keys(driver,self.khxk_picture,khxk_picture)
        object.send_keys(driver,self.yyzz_picture,yyzz_picture)
        object.click(driver,self.tijiao_button)
        # time.sleep(60)
    def get_fail_duanya_text(self,driver):
        get_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(  self.duanyan_element  )).text
        return get_text
    def get_success_duanya_text(self,driver):
        get_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located(  self.success_duanya_text  )).text
        return get_text
