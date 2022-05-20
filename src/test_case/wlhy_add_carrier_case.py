import unittest

from src.business.WLHY.login_business import LoginBusiness
from src.business.WLHY.wlhy_add_carrier_business import AddCarrierBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_carrier_page import AddCarrierPage


class AddCarrierCase(unittest.TestCase):
    def setUp(self):
        """初始化浏览器"""
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,3)
    def tearDown(self):
        self.driver.quit()

    def test_case_01(self):
        """合法添加承运商"""
        try:
            AddCarrierBusiness().add_carrier_oper(self.driver,1)
            assert_text = AddCarrierPage().add_success_assert(self.driver)
            self.assertEqual("简称",assert_text)
        except:
            GeneralMethod().get_picture(self.driver,"合法添加承运商")
            raise

    def test_case_02(self):
        """承运商已存在！"""
        try:
            AddCarrierBusiness().add_carrier_oper(self.driver,2)
            assert_text = AddCarrierPage().add_fail_assert(self.driver)
            self.assertEqual("承运商已存在！",assert_text)
        except:
            GeneralMethod().get_picture(self.driver,"承运商已存在！")
            raise