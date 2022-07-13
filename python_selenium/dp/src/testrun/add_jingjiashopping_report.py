import unittest
import os
import time
from BeautifulReport import BeautifulReport


class AddJingjiaShoppingReport:
    def test_run(self):
        # testcase_path = os.path.join(os.path.dirname(__file__),"..","testcase")
        tao_jian = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"..","testcase"),pattern="*add_jingjiashopping_test_case.py")
        report_path = os.path.join(os.path.dirname(__file__),"..","..","reports")
        get_strftime = time.strftime("%Y%m%d%H%M%S")
        report_name = get_strftime + "_dp.html"
        BeautifulReport(tao_jian).report("dp自动化测试报告",report_name,report_path)

if __name__ == '__main__':
    AddJingjiaShoppingReport().test_run()