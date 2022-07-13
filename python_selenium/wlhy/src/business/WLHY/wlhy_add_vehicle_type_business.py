from python_selenium.wlhy.src.common.get_test_file import GetTestInfo
from python_selenium.wlhy.src.pages.WLHY.wlhy_add_vehicle_type_page import AddVehicleTypePage


class AddVehicleTypeBusiness(AddVehicleTypePage):
    def add_vehicle_type_oper(self,driver,line):
        AddVehicleTypePage().click_add_button(driver)
        data = GetTestInfo().get_test_data("wlhy_add_vehicle_type_data.csv",line)
        AddVehicleTypePage().send_keys_vehicle_type(driver,data[0],data[1])
