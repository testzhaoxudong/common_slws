from selenium.webdriver.common.by import By

from python_selenium.wlhy.src.common.General_method import GeneralMethod




class DindanXinzen(GeneralMethod):
    danhao_kuang = By.CSS_SELECTOR,'id="fhdh"' #发货单号
    bianhao_kuang = By.CSS_SELECTOR,'[id="ccbh"]'#订单编号
    kehu_kuang = By.CSS_SELECTOR,'[id="customerName"]'#客户
    kehu_queren = By.XPATH,'//*[text()="东莞华润水泥有限公司"]'
    wuzi_kuang = By.CSS_SELECTOR,'[id="goodsName"]' #物资
    wuzi_queren = By.XPATH,'//*[text()="袋装水泥P·O42.5(袋装)"]'
    baozhuang_kuang = By.CSS_SELECTOR,'[class="ant-select-selection__rendered"]'#包装方式
    chehao_kuang = By.CSS_SELECTOR,'[id="truckno"]'#车号
    penma_kuang = By.CSS_SELECTOR,'[id="pmxx"]'#喷码信息
    jinchang_time = By.CSS_SELECTOR,'[id="intime"]'#进场时间
    lichang_time = By.CSS_SELECTOR,'[id="outtime"]'#离场时间
    jingzhong_kuang = By.CSS_SELECTOR,'[id="netweight"]'#净重
    daoda_time = By.CSS_SELECTOR,'[id="arrivaltime"]'#到达时间
    wancheng_time = By.CSS_SELECTOR,'[id="finishtime"]'#完成时间
    quyu_kuang = By.CSS_SELECTOR,'[id="regionName"]'#区域
    beizhu_kuang = By.CSS_SELECTOR,'[id="remark"]'#备注
    def dindan_oper(self,driver,send_value):
        object = GeneralMethod()
        object.send_keys(driver,self.danhao_kuang,send_value)
        object.send_keys(driver,self.bianhao_kuang,send_value)
        object.click(driver,self.kehu_kuang)
        object.double_click(driver,self.kehu_queren)
        object.click(driver,self.wuzi_kuang)
        object.double_click(driver,self.wuzi_queren)


