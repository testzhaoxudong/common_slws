import os
import time
import unittest
from BeautifulReport import BeautifulReport

class LoginReport:
    def case_run(self):
        case_paeh = os.path.join(os.path.dirname(__file__),"..","testcase")
        taojian = unittest.defaultTestLoader.discover(case_paeh,pattern="login_test_case.py")
        report_path = os.path.join(os.path.dirname(__file__),"..","..","reports")
        get_time_strftime = time.strftime("%Y%m%d%H%M%S")
        report_name = get_time_strftime+"ZHKS.html"
        BeautifulReport(taojian).report(description="智慧矿山管控平台自动化测试报告",filename=report_name,report_dir=report_path)


if __name__ == '__main__':
    LoginReport().case_run()


