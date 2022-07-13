import unittest

from python_selenium.wlhy.src.business.WLHY.dindan_business import DinDan_Business
from python_selenium.wlhy.src.business.WLHY.login_business import LoginBusiness
from python_selenium.wlhy.src.common.General_method import GeneralMethod
from python_selenium.wlhy.src.pages.WLHY.wlhy_dindan_page import DinDan_Page


class DinDan_Case(unittest.TestCase):
    def setUp(self):
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,1)
    def tearDown(self):
        self.driver.quit()
    def test_dindan_case01(self):
        """合法添加运单"""
        try:
            DinDan_Business().dindan_oper(self.driver,1)
            duanyan_text = DinDan_Page().add_success_assert(self.driver)
            self.assertEqual("提交成功",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增订单1")
            raise

    def test_dindan_case02(self):
        """发货人为空，其余正常填写"""
        try:
            DinDan_Business().dindan_oper(self.driver,2)
            duanyan_text = DinDan_Page().add_fhr_assert(self.driver)
            self.assertEqual("请输入发货人",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增订单1")
            raise
    def test_dindan_case03(self):
        """输入发货人手机号格式非法，其余正常填写"""
        try:
            DinDan_Business().dindan_oper(self.driver,3)
            duanyan_text = DinDan_Page().get_assert_text(self.driver)
            self.assertEqual("请输入正确的手机号！",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增订单1")
            raise
    def test_dindan_case04(self):
        """物资单价输入负数，其余正常填写"""
        try:
            DinDan_Business().dindan_oper(self.driver,4)
            duanyan_text = DinDan_Page().get_assert_text(self.driver)
            self.assertEqual("请输入正确的数字！",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增订单1")
            raise
