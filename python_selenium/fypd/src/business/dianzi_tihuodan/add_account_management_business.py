from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.dainzi_tihuodan.add_account_management_page import AddAccountManagementPage


class AddAccountManagementBusiness(AddAccountManagementPage):
    def add_account_management_save_function(self,driver,line):
        # AddAccountManagementPage().add(driver)
        data = GetTestInfo().get_test_data("add_account_management_test_case_data.csv",line)
        AddAccountManagementPage().add_account_management_save_oper(driver,data[0],data[1],data[2],data[3])
    def add_account_management_canel_function(self,driver,line):
        # AddAccountManagementPage().add(driver)
        data = GetTestInfo().get_test_data("add_account_management_test_case_data.csv",line)
        AddAccountManagementPage().add_account_management_save_oper(driver,data[0],data[1],data[2],data[3])
