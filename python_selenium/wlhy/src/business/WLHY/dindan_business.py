from python_selenium.wlhy.src.common.get_test_file import GetTestInfo
from python_selenium.wlhy.src.pages.WLHY.wlhy_dindan_page import DinDan_Page


class DinDan_Business(DinDan_Page):
    def dindan_oper(self,driver,line):
        data = GetTestInfo().get_test_data("wlhy_dindan_data.csv",line)
        object = DinDan_Page()
        object.xinzeng_click(driver)
        object.send_keys_dindna_data(driver,data[0],data[1],data[2],data[3],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13])



