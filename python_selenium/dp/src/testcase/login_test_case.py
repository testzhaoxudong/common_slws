import unittest
from python_selenium.dp.src.business.login_business import LoginBusiness
from python_selenium.dp.src.common.currency import Common
from python_selenium.dp.src.common.get_test_info import Get_Test_Info
from python_selenium.dp.src.pages.login_page import Login_Page


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.Wait = Common().init_driver("dp_url.csv","dp_pc_url")
    def tearDown(self):
        self.driver.quit()
    def test_correct_username_password(self):
        """合法登陆自动化测试用例"""
        try:
            LoginBusiness().login_function(self.driver,1)
            get_assert_txt = Login_Page().get_login_success_assert_text(self.driver)
            assert_text = Get_Test_Info().get_test_data("login_data.csv",1)
            self.assertEqual(assert_text[2],get_assert_txt,"正常登录成功")
        except:
            Common().get_screenshot("合法登陆自动化测试用例",self.driver)
            raise
    def test_correct_username_error_password(self):
        """使用正确的用户名错误密码登录"""
        try:
            LoginBusiness().login_function(self.driver,2)
            get_assert_txt = Login_Page().get_login_fail_assert_text(self.driver)
            assert_text = Get_Test_Info().get_test_data("login_data.csv",2)
            self.assertEqual(assert_text[2],get_assert_txt,"错误密码登录")
        except:
            Common().get_screenshot("使用正确的用户名错误密码登录",self.driver)
            raise
    def test_error_username_correct_password(self):
        """使用正确的用户名错误密码登录"""
        try:
            LoginBusiness().login_function(self.driver,3)
            get_assert_txt = Login_Page().get_login_fail_assert_text(self.driver)
            assert_text = Get_Test_Info().get_test_data("login_data.csv",3)
            self.assertEqual(assert_text[2],get_assert_txt,"错误用户名登录")
        except:
            Common().get_screenshot("使用错误用户名正确密码登录",self.driver)
            raise

