import unittest

from python_selenium.dp.src.business.login_business import LoginBusiness
from python_selenium.dp.src.business.out_jingjiashopping_business import OutJingjiaShoppingBusiness
from python_selenium.dp.src.common.currency import Common


class OutJingjiaShoppingTestCase(unittest.TestCase):
    def setUp(self):
        self.driver,self.wait = Common().init_driver("dp_url.csv","dp_pc_url")
        LoginBusiness().yuzhi_login_function(self.driver,1)
    def tearDown(self):
        self.driver.quit()
    def test_outjshopping_case(self):
        try:
            OutJingjiaShoppingBusiness().out_jjshopping_oper(self.driver,1)
            # assert_text = Get_Test_Info().get_test_data("add_jingjia_data",1)
            # get_assert_text = AddJingjiaShoppingPage().get_success_assert_text(self.driver)
            # self.assertEqual(assert_text[14],get_assert_text)
        except:
            Common().get_screenshot("发布商品",self.driver)
            raise

