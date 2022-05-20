from src.common.get_test_file import GetTestInfo
from src.pages.WLHY.wlhy_add_hz_page import AddHzPage


class AddHzBusiness(AddHzPage):
    def add_hz_oper(self,driver,line):
        object = AddHzPage()
        object.xinzeng_click(driver)
        data = GetTestInfo().get_test_data("wlhy_add_hz_data.csv",line)
        object.send_keys_hz_data(driver,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14])