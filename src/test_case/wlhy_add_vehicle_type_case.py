import unittest

from src.business.WLHY.login_business import LoginBusiness
from src.business.WLHY.wlhy_add_vehicle_type_business import AddVehicleTypeBusiness
from src.common.General_method import GeneralMethod
from src.pages.WLHY.wlhy_add_vehicle_type_page import AddVehicleTypePage


class AddVehicleTypeCase(unittest.TestCase):
    def setUp(self):
        """初始化浏览器"""
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,3)
    def tearDown(self):
        self.driver.quit()
    def test_case_01(self):
        """ 合法新增车辆类型"""
        try:
            AddVehicleTypeBusiness().add_vehicle_type_oper(self.driver,1)
            assert_text = AddVehicleTypePage().add_success_assert(self.driver)
            self.assertEqual("提交成功",assert_text)
        except:
            GeneralMethod().get_picture(self.driver,"合法新增车辆类型")
            raise

    def test_case_02(self):
        """ 辆类型编码重复，保存失败"""
        try:
            AddVehicleTypeBusiness().add_vehicle_type_oper(self.driver,2)
            assert_text = AddVehicleTypePage().add_fail_assert(self.driver)
            self.assertEqual("车辆类型编码重复，保存失败",assert_text)
        except:
            GeneralMethod().get_picture(self.driver,"辆类型编码重复，保存失败")
            raise

