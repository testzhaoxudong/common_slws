from selenium.webdriver.common.by import By

from python_selenium.dp.src.common.currency import Common


class Add_XSShopping_page(Common):
    shopping_admin = By.XPATH,'//*[text()="商城管理"]'  #商城管理
    sp_admin = By.XPATH,'//*[text()="商品管理"]'        #商品管理
    xsshopping = By.XPATH,'//*[text()="协商商品"]'      #协商商品
    add_button = By.XPATH,'//*[text()="新 增"]'         #新增按钮
    jg = By.XPATH,'//*[text()="请选择所属机构"]'

