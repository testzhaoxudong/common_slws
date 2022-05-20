import unittest
from src.business.WLHY.login_business import LoginBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_login import LoginPage


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
    def tearDown(self):
        self.driver.quit()
    # 用例一：正常登录用例
    def test_normal_login(self):
        "登录成功，断言成功"
        try:
            LoginBusiness().login_function(self.driver,3)
            duanyan_text = LoginPage().login_success_assert(self.driver)
            self.assertEqual("首页",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"正常登录用例")
            raise
    def test_normal_login_1(self):
        "登录失败，断言成功"
        try:
            LoginBusiness().login_function(self.driver,2)
            duanyan_text = LoginPage().login_abnormal_assert(self.driver)
            self.assertEqual("用户名或密码错误",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"异常")
            raise

