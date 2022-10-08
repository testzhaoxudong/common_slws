from python_selenium.fypd.src.common.get_test_info import GetTestInfo
from python_selenium.fypd.src.pages.dainzi_tihuodan.add_tihuodan_management_page import AddTihuodanManagementPage


class AddTihuodanManagementBusiness(AddTihuodanManagementPage):
    def add_tihuodan_management_function(self,driver,line):
        testcase_data = GetTestInfo().get_test_data("add_tihuodan_management_test_data.csv",line)
        AddTihuodanManagementPage().add_tihuodan_management_save_oper(driver,line,testcase_data[1],testcase_data[2],testcase_data[3])
