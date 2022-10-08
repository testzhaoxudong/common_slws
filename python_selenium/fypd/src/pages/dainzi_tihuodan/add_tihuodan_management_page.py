from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep

from selenium.webdriver.common.by import By

from python_selenium.fypd.src.common.common_code import CommonCode
from python_selenium.fypd.src.common.get_test_info import GetTestInfo


class AddTihuodanManagementPage(CommonCode):
    dianzi_tihuodan = By.XPATH, '//*[@id="root"]/div/section/div/aside/div/ul/li[4]'  # 电子提货单【4】
    tihuodan_management = By.LINK_TEXT,'提货单管理'
    add_button = By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/button[1]'

    materialNo = By.ID,"materialNo"             #物资
    materialNo_1 = By.XPATH, '//li[text()="10-8系统测试物资"]'
    materialNo_2 = By.XPATH, '//li[text()="大块"]'
    materialNo_3 = By.XPATH, '//li[text()="大块1"]'
    materialNo_4 = By.XPATH, '//li[text()="粉煤（门克庆车队）"]'
    materialNo_5 = By.XPATH, '//li[text()="混块"]'
    materialNo_6 = By.XPATH, '//li[text()="矸石"]'
    materialNo_7 = By.XPATH, '//li[text()="矸石5"]'

    custName = By.XPATH,'//*[@class="ant-input ant-select-search__field"]'                 #客户名称
    deliveryCount = By.ID,"deliveryCount"       #提货单张数
    plannedTonnage = By.ID,"plannedTonnage"     #计划重量
    baocun_button = By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/span/button'
    success_assert = By.XPATH,'//*[text()="操作成功"]'     #新增成功断言文本

    def add_tihuodan_management_save_oper(self,driver,line,custName_value,deliveryCount_value,plannedTonnage_value):
        object = CommonCode()
        object.click(driver,self.dianzi_tihuodan)
        object.click(driver,self.tihuodan_management)
        sleep(2)
        object.click(driver,self.add_button)

        object.click(driver,self.materialNo)
        materialNo = GetTestInfo().get_test_data("add_tihuodan_management_test_data.csv",line)
        key = materialNo[0]
        print(key)
        if key == "10-8系统测试物资":
            object.click(driver,self.materialNo_1)
        elif key == "大块":
            object.click(driver,self.materialNo_2)
        elif key == "大块1":
            object.click(driver,self.materialNo_3)
        elif key == "粉煤（门克庆车队）":
            object.click(driver,self.materialNo_4)
        elif key == "混块":
            object.click(driver,self.materialNo_5)
        elif key == "矸石":
            object.click(driver,self.materialNo_6)
        elif key == "矸石5":
            object.click(driver,self.materialNo_7)
        # sleep(1)

        """ object.click(driver,materialNo)
            element = By.XPATH,'//ul[@role="listbox"]/li'
            text_1 = driver.find_elements_by_xpath('//ul[@role="listbox"]/li')
            text_1 = WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_all_elements_located((element)))
            print(text_1.text)
            for li in text_1:
                print(li.text)
                if "粉煤（门克庆车队）" in li.text:
                    li.click()"""

        object.send_keys(driver,self.custName,custName_value)
        sleep(0.01)
        object.send_keys(driver,self.custName,Keys.ENTER)
        object.send_keys(driver,self.deliveryCount,deliveryCount_value)
        object.send_keys(driver,self.plannedTonnage,plannedTonnage_value)
        object.click(driver,self.baocun_button)

    def success_add_tihuodan_management_assert_text(self,driver):
        assert_text = WebDriverWait(driver,10,0.2).until(expected_conditions.presence_of_element_located((self.success_assert))).text
        # assert_text = CommonCode().element(driver,self.success_assert)
        return assert_text


