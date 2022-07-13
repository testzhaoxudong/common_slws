import time
from selenium.webdriver.common.by import By

from python_selenium.dp.src.common.currency import Common


class OutJingjiaShoppingPage(Common):
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
    out_button = By.XPATH,'/html/body/div/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/form/div[1]/div/text/button[2]'
    jjshh = By.XPATH,'/html/body/div/div/section/div/aside/div/ul/li[2]/ul/li[13]/a'
    shh_button = By.XPATH,'/html/body/div/div/section/section/main/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/a[2]'
    tongguo_button = By.XPATH,"/html/body/div/div/section/section/main/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]"
    quedin_button = By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]"
    fabu_button = By.XPATH,"/html/body/div[1]/div/section/section/main/div/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/span/a[2]"
    queren_fabu = By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]"

    # success_assert = By.XPATH,"<span></span>"


    def out_jjshopping_page(self,driver,activity_title_vaule,materialDesc_value,materialImg_value,qpj_value,shopping_shuliang_value,earnestMoney_value,startTime_value,endTime_value,shippedDays_value):
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
        object.click(driver,self.out_button)
        time.sleep(1)
        object.click(driver,self.jjshh)
        object.click(driver,self.shh_button)
        object.click(driver,self.tongguo_button)
        time.sleep(1)
        object.click(driver,self.quedin_button)
        time.sleep(1)
        object.click(driver,self.jj)
        time.sleep(2)
        object.click(driver,self.fabu_button)
        time.sleep(2)
        object.click(driver,self.queren_fabu)

