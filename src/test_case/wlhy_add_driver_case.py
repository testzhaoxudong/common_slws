import unittest
from src.business.WLHY.login_business import LoginBusiness
from src.business.WLHY.wlhy_add_driver_business import AddDriverBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_driver_page import AddDriverPage


class AddDriverCase(unittest.TestCase):
    def setUp(self):
        """初始化浏览器"""
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,3)
    def tearDown(self):
        self.driver.quit()

    def test_case_01(self):
        try:
            AddDriverBusiness().add_driver_oper(self.driver,1)
            assert_text = AddDriverPage().get_assert_success_text(self.driver)
            self.assertEqual("保存成功",assert_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增司机")
            raise

    def test_case_02(self):
        try:
            AddDriverBusiness().add_driver_oper(self.driver,2)
            assert_text = AddDriverPage().get_assert_fail_text(self.driver)
            self.assertEqual("该身份证号对应的司机已被添加！",assert_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增司机")
            raise