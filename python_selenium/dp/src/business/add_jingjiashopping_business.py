from python_selenium.dp.src.common.get_test_info import Get_Test_Info
from python_selenium.dp.src.pages.add_jingjiashopping_page import AddJingjiaShoppingPage


class AddJingjiaShoppingBusiness(AddJingjiaShoppingPage):
    def add_jjshopping_oper(self,driver,line):
        data = Get_Test_Info().get_test_data("add_jingjia_data",line)
        AddJingjiaShoppingPage().add_jjshopping_page(driver,data[0],data[4],data[5],data[7],data[8],data[10],data[11],data[12],data[13])
