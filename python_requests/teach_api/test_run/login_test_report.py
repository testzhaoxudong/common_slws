import os
import unittest
import time
from BeautifulReport import BeautifulReport


class  LoginTestReport:
    def testcase_run(self):
        #测试用例套件
        testcase_path = os.path.join(os.path.dirname(__file__),"..","testcase")
        taojian = unittest.defaultTestLoader.discover(testcase_path,pattern="test_teach_login_api.py")
        #测试报告
        get_strftime = time.strftime("%Y%m%d%H%M%S")
        report_name = get_strftime+"Login_api_test_report.html"
        report_path = os.path.join(os.path.dirname(__file__),"..","reports")
        #判断一下测试报告的目录是否存在如果不存在则创建一个
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        #实例化BeautifulReport对象
        BeautifulReport(taojian).report(description="登录接口测试报告",filename=report_name,report_dir=report_path)
if __name__ == '__main__':
    LoginTestReport().testcase_run()