import unittest
from selenium.webdriver.android import webdriver

from python_selenium.wlhy.src.business.scdn_b import CsdnLoginBusiness
from python_selenium.wlhy.src.common.General_method import GeneralMethod


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        #初始化浏览器对其赋值
        self.driver = webdriver.Chrome()
        self.driver.get("https://passport.csdn.net/newlogin?code=mobile")
    # 用例一：正常登录用例
    def test_normal_login(self):
        "登录成功，断言成功"
        try:
            #测试用例，输入合法的用户名和密码登录
            CsdnLoginBusiness().login_function(self.driver,1)
        except:
            #用例执行失败后截取图片
            GeneralMethod().get_picture(self.driver,"正常登录用例")
            raise
    def tearDown(self):
        # 测试用例执行完毕关闭浏览器
        self.driver.quit()