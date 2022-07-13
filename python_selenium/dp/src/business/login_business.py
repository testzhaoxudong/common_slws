from python_selenium.dp.src.common.get_test_info import Get_Test_Info
from python_selenium.dp.src.pages.login_page import Login_Page


class LoginBusiness(Login_Page):
    def login_function(self,driver,line):
        login_data = Get_Test_Info().get_test_data("login_data.csv",line)
        Login_Page().loger_oper(driver,login_data[0],login_data[1])

    def yuzhi_login_function(self,driver, line):
        login_data = Get_Test_Info().get_test_data("login_data.csv", line)
        Login_Page().loger_oper(driver, login_data[0], login_data[1])
