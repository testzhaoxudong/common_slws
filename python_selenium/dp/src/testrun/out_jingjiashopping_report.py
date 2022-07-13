import unittest
import os
import time
from BeautifulReport import BeautifulReport


class OutJingjiaShoppingReport:
    def test_run(self):
        tao_jian = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"..","testcase"),pattern="*out_jingjiashopping_test_case.py")
        report_path = os.path.join(os.path.dirname(__file__),"..","..","reports")
        get_strftime = time.strftime("%Y%m%d%H%M%S")
        report_name = get_strftime + "_OutJingjiaShoppingReport.html"
        BeautifulReport(tao_jian).report("发布竞价商品自动化测试报告",filename=report_name,report_dir=report_path)
if __name__ == '__main__':
    OutJingjiaShoppingReport().test_run()