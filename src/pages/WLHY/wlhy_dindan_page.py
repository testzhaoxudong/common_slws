import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.common.General_method import GeneralMethod


class DinDan_Page(GeneralMethod):
    wlhy = (By.XPATH,'//*[text()="网络货运"]')
    wlhy_huoyuan = (By.XPATH,'//*[@id="/network$Menu"]/li[1]/a')
    xinzeng_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/button[1]')
    fahuoren = (By.XPATH,'//*[@class="ant-input ant-select-search__field"]')
    shouhuoren = (By.XPATH,'//*[@id="receiverName"]/div/div/ul/li/div/input')
    fahuoren_phone = (By.XPATH,'//*[@id="shipperPhone"]')
    shouhuoren_phone = (By.XPATH,'//*[@id="receiverPhone"]')

    fahuodizhi = (By.XPATH,'//*[@id="shipAddressRegionName"]')
    fahuodizhi_sheng = (By.XPATH,'//*[@title="北京"]')
    fahuodizhi_shi = (By.XPATH,'//*[@title="北京市"]')
    fahuodizhi_qu = (By.XPATH,'//*[@title="东城区"]')
    fahuodizhi_xiangxi = (By.ID,"shipFullAddress")


    shouhuodizhi = (By.XPATH,'//*[@id="receiveAddressRegionName"]')
    shouhuodizhi_sheng = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[6]/div/div[1]/div[2]/div/span/div/div/div/div/ul[1]/li[2]')
    shouhuodizhi_shi = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[6]/div/div[1]/div[2]/div/span/div/div/div/div/ul[2]/li')
    shouhuodizhi_qu = (By.XPATH,'//*[@id="antd-pro-components-network-net-work-network"]/div/div[6]/div/div[1]/div[2]/div/span/div/div/div/div/ul[3]/li[2]')
    shouhuoren_code = (By.XPATH,'//*[@id="receiverNo"]')
    shouhuodizhi_xiangxi = (By.XPATH,'//*[@id="receiveFullAddress"]')

    wuzi = (By.XPATH,'//*[@id="materialName"]')
    danjia = (By.XPATH,'//*[@id="price"]')
    shuliang = (By.XPATH,'//*[@id="materialTotalnum"]')
    zongzhong = (By.XPATH,'//*//*[@id="materialTotalamount"]')
    beizhu = (By.XPATH,'//*[@id="transportNote"]')
    tijiao_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/button[1]')
    add_success_duanyan = (By.XPATH,'//*[text()="提交成功"]')
    add_abnormal_duanyan = (By.XPATH,'/ html / body / div[2] / div / span / div / div / div / div[1]')

    #断言element
    add_assert_element = (By.XPATH,'//*[@class="ant-form-explain"]')

    def xinzeng_click(self,driver):
        object = GeneralMethod()
        object.click(driver,self.wlhy)
        time.sleep(0.5)
        object.click(driver,self.wlhy_huoyuan)
        time.sleep(1)
        object.click(driver,self.xinzeng_button)
    def send_keys_dindna_data(self,driver,fahuoren_value,shouhuoren_value,fahuoren_phone_value,shouhuoren_phone_value,fxiangxi_id_value,shouhuoren_code,sxiangxi_id_value,wuzi_value,danjia_value,shuliang_value,zongzhong_value,beizhu_value):
        object = GeneralMethod()
        object.send_keys(driver,self.fahuoren,fahuoren_value)
        object.send_keys(driver,self.shouhuoren,shouhuoren_value)
        object.send_keys(driver,self.fahuoren_phone,fahuoren_phone_value)
        object.send_keys(driver,self.shouhuoren_phone,shouhuoren_phone_value)

        object.click(driver,self.fahuodizhi)
        object.click(driver,self.fahuodizhi_sheng)
        object.click(driver,self.fahuodizhi_shi)
        object.click(driver,self.fahuodizhi_qu)



        object.click(driver,self.shouhuodizhi)
        object.click(driver,self.shouhuodizhi_sheng)
        object.click(driver,self.shouhuodizhi_shi)
        object.click(driver,self.shouhuodizhi_qu)

        #发货人详细地址
        element_xiangxi = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located(self.fahuodizhi_xiangxi))
        # js2 = 'arguments[0].removeAttribute("disabled")
        js1 = 'document.getElementById("shipFullAddress").removeAttribute("disabled")'
        driver.execute_script(js1, element_xiangxi)
        element_xiangxi.send_keys(fxiangxi_id_value)

        #收货人详细地址
        element_xiangxi = WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located(self.shouhuodizhi_xiangxi))
        # js2 = 'arguments[0].removeAttribute("disabled")
        js1 = 'document.getElementById("receiveFullAddress").removeAttribute("disabled")'
        driver.execute_script(js1, element_xiangxi)
        element_xiangxi.send_keys(sxiangxi_id_value)

        object.send_keys(driver,self.shouhuoren_code,shouhuoren_code)
        object.send_keys(driver,self.wuzi,wuzi_value)
        object.send_keys(driver,self.danjia,danjia_value)
        object.send_keys(driver,self.shuliang,shuliang_value)
        object.send_keys(driver,self.zongzhong,zongzhong_value)
        object.send_keys(driver,self.beizhu,beizhu_value)
        object.click(driver,self.tijiao_button)
        # time.sleep(0.5)
        # object.click(driver,self.chaxun_button)
        # time.sleep(2)

    def add_success_assert(self,driver):
        return WebDriverWait(driver, 10, 0.2).until(expected_conditions.presence_of_element_located((self.add_success_duanyan))).text


    def add_abnormal_assert(self,driver):
        return GeneralMethod().get_text(driver,self.add_abnormal_duanyan)

    # 未输入发货人断言
    def add_fhr_assert(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_all_elements_located((self.add_assert_element)))[0].text

    #获取断言文本
    def get_assert_text(self,driver):
        return WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_all_elements_located((self.add_assert_element)))[0].text