from src.common.get_test_file import GetTestInfo
from src.pages.WLHY.wlhy_add_carrier_page import AddCarrierPage


class AddCarrierBusiness(AddCarrierPage):
    def add_carrier_oper(self,driver,line):
        AddCarrierPage().click_add_buttom(driver)
        data = GetTestInfo().get_test_data("wlhy_add_carrier_data.csv",line)
        AddCarrierPage().send_keys_carrier(driver,data[0],data[1],data[2],data[3],data[4],data[5],data[6])
