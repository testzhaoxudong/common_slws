from python_appium.mht_kuangjia.business.action import huadong
from python_appium.mht_kuangjia.config.mht_capabilities import getDriver
from time import sleep


def shezhi(appDriver):
    #点击设置按钮
    sleep(2)
    appDriver.find_element_by_id("com.emicro.emicrophone:id/guidehead_right_layout").click()
    sleep(2)
    #点击设置
    appDriver.find_element_by_id("com.emicro.emicrophone:id/menu_setting").click()
    sleep(2)

if __name__ == '__main__':
    driver = getDriver(False)
    huadong(driver)
    shezhi(driver)