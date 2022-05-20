import unittest
from src.business.WLHY.login_business import LoginBusiness
from src.business.WLHY.wlhy_add_hz_business import AddHzBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_hz_page import AddHzPage


class AddHzCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,3)
    def tearDown(self):
        self.driver.quit()
    def test_case_01(self):
        """合法新增，新增成功"""
        try:
            AddHzBusiness().add_hz_oper(self.driver,1)
            duanyan_text = AddHzPage().get_success_duanya_text(self.driver,)
            self.assertEqual("提交成功",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增货主账号")
            raise
    def test_case_02(self):
        """该客户名称已存在，请检查!"""
        try:
            AddHzBusiness().add_hz_oper(self.driver,2)
            duanyan_text = AddHzPage().get_fail_duanya_text(self.driver,)
            self.assertEqual("该客户名称已存在，请检查!",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增货主账号")
            raise

    def test_case_03(self):
        """该统一社会信用代码已经存在，请检查!"""
        try:
            AddHzBusiness().add_hz_oper(self.driver,3)
            duanyan_text = AddHzPage().get_fail_duanya_text(self.driver,)
            self.assertEqual("该统一社会信用代码已经存在，请检查!",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增货主账号")
            raise

    def test_case_04(self):
        """登录用户名已存在"""
        try:
            AddHzBusiness().add_hz_oper(self.driver,4)
            duanyan_text = AddHzPage().get_fail_duanya_text(self.driver,)
            self.assertEqual("该登录用户名已存在，请检查!",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增货主账号")
            raise

    def test_case_05(self):
        """联系电话已经存在，请检查!"""
        try:
            AddHzBusiness().add_hz_oper(self.driver,5)
            duanyan_text = AddHzPage().get_fail_duanya_text(self.driver,)
            self.assertEqual("该联系电话已经存在，请检查!",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增货主账号")
            raise