import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_selenium.dp.src.common.currency import Common


class AddJingjiaShoppingPage(Common):
    mall_admin = By.XPATH,'//*[text()="商城管理"] '
    jj = By.XPATH,'/html/body/div/div/section/div/aside/div/ul/li[2]/ul/li[12]/a'
    add_button = By.XPATH,'//*[@class="ant-btn ant-btn-primary" and @type="button"] '

    activity_title = By.ID,'activityTitle'#活动标题
    jg = By.ID,'factoryId'#所属机构
    jg_name = By.XPATH,'//*[text()="达顺石料厂"] '
    materialName = By.ID,'materialName'#竞价商品
    shopp = By.XPATH,'//*[@title="竞价测试物资"]'
    queren_button = By.XPATH,'//*[text()="确 认"]' #商品确认
    materialDesc = By.ID,'materialDesc'#商品介绍
    materialImg = By.ID,'materialImg'#商品图片
    biddingWay = By.ID,'biddingWay'#竞价方式
    gkjj = By.XPATH,'//*[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]' #公开竞价
    qpj = By.ID,'biddingStartPrice'    #起拍价
    shopping_shuliang = By.ID,'materialTotal'  #商品数量
    unit = By.ID,'unit'  #计量单位
    earnestMoney = By.ID,'earnestMoney' #保证金
    startTime = By.ID,'startTime' #开始时间
    send_staertime = By.XPATH,'// *[ @class ="ant-calendar-input "]'
    startTime_quedin = By.XPATH,'//*[@class="ant-calendar-ok-btn"]'
    endTime = By.ID,'endTime' #结束时间
    send_endtime = By.XPATH,'//*[@class="ant-calendar-input "]'
    endTime_quedin = By.XPATH,'//*[@class="ant-calendar-ok-btn"]'
    shippedDays = By.ID,'shippedDays' #发运天数
    end = By.XPATH,'//*[@class="ant-btn ant-btn-primary"]'

    success_assert = By.XPATH,'/html/body/div[2]/div/span'

    def add_jjshopping_page(self,driver,activity_title_vaule,materialDesc_value,materialImg_value,qpj_value,shopping_shuliang_value,earnestMoney_value,startTime_value,endTime_value,shippedDays_value):
        object = Common()
        object.click(driver,self.mall_admin)
        time.sleep(0.5)
        object.click(driver,self.jj)
        object.click(driver,self.add_button)

        object.send_keys(driver, self.activity_title, activity_title_vaule)
        object.click(driver,self.jg)
        object.click(driver,self.jg_name)
        object.click(driver,self.materialName)
        object.click(driver,self.shopp)
        object.double_click(driver,self.queren_button)

        object.send_keys(driver, self.materialDesc,materialDesc_value)
        object.send_keys(driver, self.materialImg,materialImg_value)

        object.click(driver,self.biddingWay)
        object.click(driver,self.gkjj)

        object.send_keys(driver, self.qpj,qpj_value)
        object.send_keys(driver, self.shopping_shuliang,shopping_shuliang_value)
        object.send_keys(driver, self.earnestMoney,earnestMoney_value)
        object.click(driver,self.startTime)
        object.send_keys(driver, self.send_staertime,startTime_value)
        object.click(driver,self.startTime_quedin)
        time.sleep(0.5)
        object.click(driver,self.endTime)
        object.send_keys(driver, self.send_endtime,endTime_value)
        object.click(driver,self.endTime_quedin)
        object.send_keys(driver, self.shippedDays,shippedDays_value)

        object.click(driver,self.end)

    def get_success_assert_text(self,driver):
        # Common().get_text(driver,self.success_assert)
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.success_assert))).text



