import os
import unittest
from BeautifulReport import BeautifulReport
import time


class LoginReport:
    #获取测试套件（测试用例）
    testcase_path = os.path.join(os.path.dirname(__file__),"..","..","test_case","other")
    tao_jian = unittest.defaultTestLoader.discover(testcase_path,pattern="*login_case.py")
    #测试报告命名
    get_system_time = time.strftime("%Y%m%d%H%M%S")
    report_name = get_system_time + "LoginReport" + ".html"
    #获取测试报告存放位置
    report_path = os.path.join(os.path.dirname(__file__),"..","..","..","report")
    BeautifulReport(tao_jian).report(description="wypd_login_test_report",filename=report_name,report_dir=report_path)