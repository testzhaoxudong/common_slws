import unittest
from python_selenium.fypd.src.business.other.login_business import LoginBusiness
from python_selenium.fypd.src.common.common_code import CommonCode
from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.other.login_page import LoginPage


class TestLoginCase(unittest.TestCase):

    #测试准备，初始化浏览器，输入url。执行每条测试用例的时候都要执行一次
    def setUp(self):
        self.driver,self.wait = CommonCode().init_driver("pc_url")

    #善后处理，关闭浏览器。执行每条测试用例的时候都要执行一次
    def tearDown(self):
        self.driver.quit()
    #用例一：合法登录，使用正确的用户名和正确的密码登录
    def test_correct_username_correct_password_login(self):
        """合法登录，使用正确的用户名和正确的密码登录"""
        try:
            #实例化LoginBusiness，调用LoginBusiness中的login_function登录功能方法，进行登录功能的测试并读取第一行测试用例
            LoginBusiness().login_function(self.driver,1)
            #断言：获取实际测试结果
            actual_assert_text = LoginPage().success_assert(self.driver)
            #获取断言的预期结果
            expect_assert_text = GetTestInfo().get_test_data("login_test_case_data.csv",1)
            #使用unittest框架中的assertEqual方法进行断言（assertEqual判断实际测试结果是否与预计结果一致）
            self.assertEqual(expect_assert_text[2],actual_assert_text)
        except:
            #获取执行失败的截图
            CommonCode().get_screenshot(self.driver,"test_correct_username_correct_password_login")
            raise #抛出执行错误信息
    #用例二：非法登录，使用错误的用户名正确的密码
    def test_error_username_correct_password_login(self):
        """使用错误的用户名正确的密码"""
        try:
            LoginBusiness().login_function(self.driver,2)
            actual_assert_text = LoginPage().fail_assert(self.driver)
            expect_assert_text = GetTestInfo().get_test_data("login_test_case_data.csv",2)
            self.assertEqual(actual_assert_text,expect_assert_text[2])
        except:
            CommonCode().get_screenshot(self.driver,"test_error_username_correct_password_login")
            raise
    #用例三：非法登录，使用正确的用户名错误的密码
    def test_correct_username_error_password_login(self):
        """使用正确的用户名错误的密码"""
        try:
            LoginBusiness().login_function(self.driver,3)
            actual_assert_text = LoginPage().fail_assert(self.driver)
            expect_assert_text = GetTestInfo().get_test_data("login_test_case_data.csv",3)
            self.assertEqual(actual_assert_text,expect_assert_text[2])
        except:
            CommonCode().get_screenshot(self.driver,"test_correct_username_error_password_login")
            raise


