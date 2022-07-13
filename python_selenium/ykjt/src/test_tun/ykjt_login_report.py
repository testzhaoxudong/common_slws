import os
import unittest
import time
from BeautifulReport import BeautifulReport

class YkjtLoginReport():
    def ykjt_login_test_report(self):
        testcase_path = os.path.join(os.path.dirname(__file__),"..","test_case")
        test_cast = unittest.defaultTestLoader.discover(testcase_path,pattern="test_login_case.py")
        report_path = os.path.join(os.path.dirname(__file__),"..","..","reports","login_report")
        get_time_strftime = time.strftime("%Y%m%y%H%M%S")
        report_name = get_time_strftime + "login_test_report" + ".html"
        BeautifulReport(test_cast).report(description="兖矿登录自动化测试报告",filename=report_name,report_dir=report_path)


if __name__ == '__main__':
    YkjtLoginReport().ykjt_login_test_report()













