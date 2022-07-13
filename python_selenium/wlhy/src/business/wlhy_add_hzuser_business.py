from python_selenium.wlhy.src.common.get_test_file import GetTestInfo
from python_selenium.wlhy.src.pages.WLHY.wlhy_add_hzuser_page import AddHzuserPage


class AddhzuserBusiness(AddHzuserPage):
    def add_hzuser_oper(self,driver,line):
        AddHzuserPage().click_add_hzuser_page(driver)
        data = GetTestInfo().get_test_data("wlhy_add_hzuser_data.csv",line)
        AddHzuserPage().add_hzuser_page(driver,data[0],data[1],data[2],data[3])