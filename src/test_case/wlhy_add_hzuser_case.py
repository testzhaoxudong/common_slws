import unittest
from src.business.WLHY.login_business import LoginBusiness
from src.business.wlhy_add_hzuser_business import AddhzuserBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_hzuser_page import AddHzuserPage


class AddhzuserCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,3)
    def tearDown(self):
        self.driver.quit()

    def test_user_case01(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver,1)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver,"test_user_case01")
            raise

    def test_user_case02(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 2)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case02")
            raise

    def test_user_case03(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 3)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case03")
            raise

    def test_user_case04(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 4)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case04")
            raise

    def test_user_case05(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 5)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case05")
            raise

    def test_user_case06(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 6)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case06")
            raise

    def test_user_case07(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 7)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case07")
            raise

    def test_user_case08(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 8)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case08")
            raise

    def test_user_case09(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 9)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case09")
            raise

    def test_user_case10(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 10)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case10")
            raise

    def test_user_case11(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 11)
            duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            print(duanyan_test)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case11")
            raise

    def test_user_case12(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 12)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case12")
            raise

    def test_user_case13(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 13)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case13")
            raise

    def test_user_case14(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 14)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case014")
            raise

    def test_user_case15(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 15)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case015")
            raise

    def test_user_case16(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 16)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case16")
            raise

    def test_user_case17(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 17)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case17")
            raise

    def test_user_case18(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 18)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case18")
            raise

    def test_user_case19(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 19)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case19")
            raise

    def test_user_case20(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 20)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case020")
            raise

    def test_user_case21(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 21)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case21")
            raise

    def test_user_case22(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 22)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case22")
            raise

    def test_user_case23(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 23)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case23")
            raise

    def test_user_case24(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 24)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case24")
            raise

    def test_user_case25(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 25)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case25")
            raise

    def test_user_case26(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 26)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case26")
            raise

    def test_user_case27(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 27)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case27")
            raise

    def test_user_case28(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 28)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case28")
            raise

    def test_user_case29(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 29)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case29")
            raise

    def test_user_case30(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 30)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case30")
            raise

    def test_user_case31(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 31)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case31")
            raise

    def test_user_case32(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 32)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case32")
            raise

    def test_user_case33(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 33)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case33")
            raise

    def test_user_case34(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 34)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case34")
            raise

    def test_user_case35(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 35)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case35")
            raise

    def test_user_case36(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 36)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case36")
            raise

    def test_user_case37(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 37)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case37")
            raise

    def test_user_case38(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 38)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case38")
            raise

    def test_user_case39(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 39)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case39")
            raise

    def test_user_case40(self):
        try:
            AddhzuserBusiness().add_hzuser_oper(self.driver, 40)
            # duanyan_test = AddHzuserPage().get_duanyan_text(self.driver)
            # self.assertEqual("操作成功",duanyan_test)
        except:
            GeneralMethod().get_picture(self.driver, "test_user_case40")
            raise

