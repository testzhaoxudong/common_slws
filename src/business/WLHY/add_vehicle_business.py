from src.common.get_test_file import GetTestInfo
from src.pages.WLHY.wlhy_add_vehicle_page import Add_Vehicle_Page


class AddVehicleBusiness(Add_Vehicle_Page):
    def vehicle_oper(self,driver,line):
        data = GetTestInfo().get_test_data("wlhy_add_vehicle_data.csv",line)
        Add_Vehicle_Page().add_click(driver)
        Add_Vehicle_Page().vehicle_info(driver,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17])




