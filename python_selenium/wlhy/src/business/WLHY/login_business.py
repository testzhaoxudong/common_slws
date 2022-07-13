from python_selenium.wlhy.src.common.get_test_file import GetTestInfo
from python_selenium.wlhy.src.pages.WLHY.wlhy_login import LoginPage


class LoginBusiness(LoginPage):
    def login_function(self,driver,line):
        data = GetTestInfo().get_test_data("login_data.csv",line)
        LoginPage().login_oper(driver,data[0],data[1])

    def yuzhi_login(self,driver,line):
        data = GetTestInfo().get_test_data("login_data.csv", line)
        LoginPage().login_oper(driver, data[0], data[1])







