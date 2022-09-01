from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.other.login_page import LoginPage

class LoginBusiness(LoginPage):
    #登录业务功能方法。实现完整的登录功能
    def login_function(self,driver,line):
        login_data = GetTestInfo().get_test_data("login_test_case_data.csv",line)
        LoginPage().login_oper(driver,login_data[0],login_data[1])

    #预置登录方法，其他功能使用
    def yuzhi_login_function(self,driver,line):
        login_data = GetTestInfo().get_test_data("login_test_case_data.csv",line)
        LoginPage().login_oper(driver,login_data[0],login_data[1])