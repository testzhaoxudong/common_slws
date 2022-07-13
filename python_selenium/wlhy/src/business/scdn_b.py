from python_selenium.wlhy.src.common.get_test_file import GetTestInfo
from python_selenium.wlhy.src.pages.csdn_page import CsdnLoginPage


class CsdnLoginBusiness(CsdnLoginPage):
    def login_function(self,driver,line):
        #读取测试数据
        data = GetTestInfo().get_test_data("login_data.csv",line)
        CsdnLoginPage().csdn_login_page(driver,data[0],data[1])