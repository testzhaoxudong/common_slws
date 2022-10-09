import os
import unittest

from BeautifulReport import BeautifulReport

import time
class AddAccountManagementReport:
    def testcase_run(self):
        #获取测试用例存放地址
        testcase_path = os.path.join(os.path.dirname(__file__),"..","..","test_case","dianzi_tihuodan")
        #使用unittest方法获取测试套件
        taojian = unittest.defaultTestLoader.discover(testcase_path,pattern="test_add_b_account_management_case.py")
        #获取时间戳用来给自测报告命名
        get_strftime = time.strftime("%Y%m%d%H%M%S")
        report_name = get_strftime + "AddAccountManagementReport" + ".html"
        #获取测试报告存放位置
        report_path = os.path.join(os.path.dirname(__file__),"..","..","..","report")
        #使用 beautifulreport插件形成测试报告
        BeautifulReport(taojian).report("AddAccountManagementReport",filename=report_name,report_dir=report_path)

if __name__ == '__main__':
      AddAccountManagementReport().testcase_run()