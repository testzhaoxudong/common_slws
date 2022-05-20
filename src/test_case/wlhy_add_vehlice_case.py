import unittest
from src.business.WLHY.add_vehicle_business import AddVehicleBusiness
from src.business.WLHY.login_business import LoginBusiness
from src.common.General_method import GeneralMethod


class Add_Vehlice_Case(unittest.TestCase):
    def setUp(self):
        self.driver,self.Wait = GeneralMethod().chushihua_driver("wlhy_url")
        """预置登录"""
        LoginBusiness().yuzhi_login(self.driver,3)
    def tearDown(self):
        self.driver.quit()
    def test_case_01(self):
        """合法添加车辆"""
        try:
            AddVehicleBusiness().vehicle_oper(self.driver,1)

            # self.assertEqual("提交成功",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver,"新增车辆")
            raise

    def test_case_02(self):
        """添加已有的车辆"""
        try:
            AddVehicleBusiness().vehicle_oper(self.driver, 1)

            # self.assertEqual("提交成功",duanyan_text)
        except:
            GeneralMethod().get_picture(self.driver, "新增车辆")
            raise


