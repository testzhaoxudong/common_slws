from src.common.get_test_file import GetTestInfo
from src.pages.WLHY.wlhy_add_driver_page import AddDriverPage


class AddDriverBusiness(AddDriverPage):
    def add_driver_oper(self,driver,line):
        AddDriverBusiness().click_add_driver(driver)
        data = GetTestInfo().get_test_data("wlhy_add_driverz_data.csv",line)
        AddDriverBusiness().send_keys_driver_data(driver,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14])
