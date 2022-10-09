import unittest

from python_selenium.fypd.src.business.dianzi_tihuodan.add_customer_management_business import \
    AddCustomerManagementBusiness
from python_selenium.fypd.src.business.other.login_business import LoginBusiness
from python_selenium.fypd.src.common.common_code import CommonCode
from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.dainzi_tihuodan.add_customer_management_page import AddCustomerManagementPage


class AddCustomerManagementTestCase(unittest.TestCase):

    def setUp(self):
        # 初始化浏览器
        self.driver,self.wait = CommonCode().init_driver("pc_url")
        #预置登录
        LoginBusiness().yuzhi_login_function(self.driver,1)
    def tearDown(self):
        #善后操作退出浏览器
        self.driver.quit()
    #用例一：合法添加客户信息，所有参数正确填写并点击保存按钮
    def test_add_customer_management_save_case(self):
        """合法添加客户信息，所有参数正确填写并点击保存按钮"""
        try:
            #执行测试操作
            AddCustomerManagementBusiness().add_customer_management_save_function(self.driver,1)
            #获取预期结果断言文本
            get_expect_assert_text = GetTestInfo().get_test_data("add_customer_management_test_case_data.csv",1)
            #获取实际测试结果
            get_actual_assert_text = AddCustomerManagementPage().add_customer_management_success_text(self.driver)
            self.assertEqual(get_expect_assert_text[-1],get_actual_assert_text)
        except:
            #截图
            CommonCode().get_screenshot(self.driver,"test_add_customer_management_save_case")
            #抛出错误结果
            raise


