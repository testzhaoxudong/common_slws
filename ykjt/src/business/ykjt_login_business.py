from ykjt.src.commin.get_ykjt_test_info import GetYkjtTestInfo
from ykjt.src.pages.ykjt_login_page import YkjtLoginPage


class YkjtLoginBusiness(YkjtLoginPage):
    def ykjt_login_oper(self,driver,line):
        data = GetYkjtTestInfo().get_test_data("ykjt_login_data.csv",line)
        YkjtLoginPage().ykjt_login(driver,data[0],data[1])
