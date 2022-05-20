import os
import unittest
import time
from BeautifulReport import BeautifulReport
class AddDindanReport():
    def run_case(self):
        case_path = os.path.join(os.path.dirname(__file__),"..","..","test_case")
        tao_jian = unittest.defaultTestLoader.discover(case_path,pattern="wlhy_dindan_test_case.py")
        report_path = os.path.join(os.path.dirname(__file__),"..","..","..","reports")
        get_time = time.strftime("%Y%m%d%H%M%S")
        report_name = get_time+"AddDindanReport.html"
        BeautifulReport(tao_jian).report(description="WLHY的自动化测试报告",filename=report_name,report_dir=report_path )

if __name__ == '__main__':
    AddDindanReport().run_case()