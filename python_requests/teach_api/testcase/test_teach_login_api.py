import unittest
from parameterized import parameterized
from python_requests.teach_api.common.get_excel_testcase_data import get_api_testcase_data
from python_requests.teach_api.common.teach_lesson_manage_api import Teach_Lesson_Manage_Api


class LoginApi(unittest.TestCase):
    #定义一个方法用来获取登录数据
    @parameterized.expand(get_api_testcase_data("teach_testcase_data.xlsx","登录"))
    def test_teach_login_api(self,data,login_testcase_retcode,logintest_num,logintest_title):
        #把测试标题写入到测试报告中
        self.logintest_title = logintest_title
        #把测试编号写入到测试报告中
        self.logintest_num = logintest_num
        #响应结果
        res = Teach_Lesson_Manage_Api().teach_login_api(data)
        #获取响应结果中的retcode的值
        res_retcode = res["retcode"]
        #获取接口测试用例中的retcode的值
        testcase_retcode = json (login_testcase_retcode["retcode"])
        if "reason" in login_testcase_retcode:
            #获取预期结果中的reason
            testcase_reason = login_testcase_retcode["reason"]
            #获取实际响应结果中的reason
            res_reason = res["reason"]
            #断言
            self.assertEqual(testcase_retcode,res_retcode)
            self.assertEqual(testcase_reason,res_reason)
        else:
            self.assertEqual(res_retcode,testcase_retcode,msg=f"实际结果中的retcode与预期结果中的retcode不一致，实际retcode为：{res_retcode}")

if __name__ == '__main__':
    LoginApi().test_teach_login_api()


