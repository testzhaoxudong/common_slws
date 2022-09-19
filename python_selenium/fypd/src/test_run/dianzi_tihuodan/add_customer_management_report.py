import os
import unittest
from BeautifulReport import BeautifulReport
import time
from python_selenium.fypd.src.common.common_code import CommonCode


class AddCustomerManagementReport:
    def add_customer_management_report(self):
        get_time = time.strftime("%Y%m%d%H%M%S")
        repoer_name = get_time + "AddCustomerManagementReport" + ".html"
        report_path = os.path.join(os.path.dirname(__file__),"..","..","..","report")
        testcase_path = os.path.join(os.path.dirname(__file__),"..","..","test_case","dianzi_tihuodan")
        taojian = unittest.defaultTestLoader.discover(testcase_path,pattern='test_add_customer_management_case.py')
        BeautifulReport(taojian).report("AddCustomerManagementReport",filename=repoer_name,report_dir=report_path)
