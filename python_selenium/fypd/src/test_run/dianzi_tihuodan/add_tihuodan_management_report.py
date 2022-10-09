import os
import unittest

from BeautifulReport import BeautifulReport

import time


class AddTihuodanManagementReport:
    def testcase_run(self):
        testcase_path = os.path.join(os.path.dirname(__file__),"..","..","test_case","dianzi_tihuodan")
        kit = unittest.defaultTestLoader.discover(testcase_path,pattern="test_add_c_tihuodan_management_case.py")
        report_path = os.path.join(os.path.dirname(__file__),"..","..","..","report")
        get_strftime = time.strftime("%Y%m%d%H%M%S")
        report_name = get_strftime + "AddTihuodanManagementReport" + ".html"
        BeautifulReport(kit).report("AddTihuodanManagementReport",filename=report_name,report_dir=report_path)
if __name__ == '__main__':
    AddTihuodanManagementReport().testcase_run()