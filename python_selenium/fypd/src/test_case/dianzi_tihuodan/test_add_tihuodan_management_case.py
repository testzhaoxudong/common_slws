import unittest

from python_selenium.fypd.src.business.dianzi_tihuodan.add_tihuodan_management_business import \
    AddTihuodanManagementBusiness
from python_selenium.fypd.src.business.other.login_business import LoginBusiness
from python_selenium.fypd.src.common.common_code import CommonCode
from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.dainzi_tihuodan.add_tihuodan_management_page import AddTihuodanManagementPage


class TestAddTihuodanManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.wait = CommonCode().init_driver("pc_url")
        LoginBusiness().yuzhi_login_function(self.driver,1)
    def tearDown(self):
        self.driver.quit()
    def test_correct_add_tihuodan_management_case(self):
        """用例一：合法新增提货单，煤种为【大块】"""
        try:
            AddTihuodanManagementBusiness().add_tihuodan_management_function(self.driver,1)
            get_expected_assert_text = GetTestInfo().get_test_data("add_tihuodan_management_test_data.csv",1)
            get_actual_assert_text = AddTihuodanManagementPage().success_add_tihuodan_management_assert_text(self.driver)
            self.assertEqual(get_expected_assert_text[-1],get_actual_assert_text)
        except:
            CommonCode().get_screenshot(self.driver,"test_correct_add_tihuodan_management_case")
            raise