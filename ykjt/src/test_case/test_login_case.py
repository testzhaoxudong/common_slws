import unittest
from datetime import time

from ykjt.src.business.ykjt_login_business import YkjtLoginBusiness
from ykjt.src.commin.get_ykjt_test_info import GetYkjtTestInfo
from ykjt.src.commin.ykjt_common import Common
from ykjt.src.pages.ykjt_login_page import YkjtLoginPage


class YkjtLoginCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.wait = Common().chushihua_driver("ykjt_url.csv","ykjt_url")
    def tearDown(self):
        self.driver.quit()
    def test_normal_login_case(self):
        """使用正确的用户名和密码登录"""
        try:
            YkjtLoginBusiness().ykjt_login_oper(self.driver,1)
            text_assert = YkjtLoginPage().login_success_assert(self.driver)
            text = GetYkjtTestInfo().get_test_data("ykjt_login_data.csv",1)
            self.assertEqual(text_assert,text[2])
        except:
            Common().get_picture(self.driver,"success_login")
            raise
    def test_error_password_login_case(self):
        """使用正确的用户名和错误的密码登录"""
        try:
            YkjtLoginBusiness().ykjt_login_oper(self.driver,2)
            text_assert = YkjtLoginPage().login_fail_assert(self.driver)
            text = GetYkjtTestInfo().get_test_data("ykjt_login_data.csv",2)
            self.assertEqual(text_assert,text[2])
        except:
            Common().get_picture(self.driver,"fail_login")
            raise

    def test_error_username_login_case(self):
        """使用错误的用户名和正确的密码登录"""
        try:
            YkjtLoginBusiness().ykjt_login_oper(self.driver,3)
            text_assert = YkjtLoginPage().login_fail_assert(self.driver)
            text = GetYkjtTestInfo().get_test_data("ykjt_login_data.csv",3)
            self.assertEqual(text_assert,text[2])
        except:
            Common().get_picture(self.driver,"fail_login")
            raise
