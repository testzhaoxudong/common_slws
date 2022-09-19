import unittest

from python_selenium.fypd.src.business.dianzi_tihuodan.add_account_management_business import \
    AddAccountManagementBusiness
from python_selenium.fypd.src.business.other.login_business import LoginBusiness
from python_selenium.fypd.src.common.common_code import CommonCode
from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.dainzi_tihuodan.add_account_management_page import AddAccountManagementPage


class AddAccountManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.wait = CommonCode().init_driver("pc_url")
        LoginBusiness().yuzhi_login_function(self.driver,1)

    def tearDown(self):
        self.driver.quit()

    def test_add_account_management_save_case(self):
        """合法新增，所有参数正确填写，点击【提交】按钮"""
        try:
            AddAccountManagementBusiness().add_account_management_save_function(self.driver,1)
            get_expect_assert_text = GetTestInfo().get_test_data("add_account_management_test_case_data.csv",1)
            get_actual_assert_text = AddAccountManagementPage().add_account_management_success_text(self.driver)
            self.assertEqual(get_actual_assert_text,get_expect_assert_text[-1])
        except:
            CommonCode().get_screenshot(self.driver,"test_add_account_management_save_case")
            raise
