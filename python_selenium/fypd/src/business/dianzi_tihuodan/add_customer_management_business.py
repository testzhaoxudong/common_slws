from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.dainzi_tihuodan.add_customer_management_page import AddCustomerManagementPage


class AddCustomerManagementBusiness(AddCustomerManagementPage):
    #保存添加客户信息功能方法
    def add_customer_management_save_function(self, driver, line):
        test_data = GetTestInfo().get_test_data("add_customer_management_test_case_data.csv", line)
        AddCustomerManagementPage().add_customer_management_save_oper(driver, test_data[0], test_data[1], test_data[2],
                                                                      test_data[3], test_data[4], test_data[5],
                                                                      test_data[6])
    #取消添加客户信息功能方法
    def add_customer_management_cancel_function(self, driver, line):
        test_data = GetTestInfo().get_test_data("add_customer_management_test_case_data.csv", line)
        AddCustomerManagementPage().add_customer_management_cancel_oper(driver, test_data[0], test_data[1], test_data[2],
                                                                      test_data[3], test_data[4], test_data[5],
                                                                      test_data[6])
