import json

import requests

from python_requests.teach_api.common.get_excel_testcase_data import get_api_testcase_data
from python_requests.teach_api.common.teach_login_api import teach_login
from python_requests.teach_api.teach_config import *

class Teach_Lesson_Manage_Api:
    #获取cookie
    user_cookie = teach_login()[0]
    #登录
    def teach_login_api(self,login_data):
        teach_login_url = f"{HOST}{LOGIN_API_PATH}"
        teach_login_data = json.loads(login_data)
        res = requests.post(url=teach_login_url, data=teach_login_data)
        return res.json()
    #新增课程
    def add_lesson_api(self,lesson_data):
        add_lesson_url = f"{HOST}{ADD_LESSON_API_PATH}"
        add_lesson_data = {
            "action":"add_course",
            "data":lesson_data
        }
        res = requests.post(url=add_lesson_url,data=add_lesson_data,cookies=self.user_cookie)
        return res.json()
    #修改成功
    def change_lesson_api(self,lesson_id,lesson_data):
        change_lesson_url = f"{HOST}{CHANGE_LESSON_API}"
        change_lesson_data = {
            "action":"modify_course",
            "id":lesson_id,
            "newdata":lesson_data
        }
        res = requests.put(url=change_lesson_url,data=change_lesson_data,cookies=self.user_cookie)
        return res.json()
    #删除课程
    def delete_lesson_api(self,lesson_id):
        delete_lesson_url = f"{HOST}{DELETE_LESSON_API_PATH}"
        delete_lesson_data = {
            "action":"delete_course",
            "id":lesson_id
        }
        res = requests.delete(url=delete_lesson_url,data=delete_lesson_data,cookies=self.user_cookie)
        return res.json()
    #查询课程
    def select_lesson_api(self,pagenum,pagesize):
        select_lesson_url = f"{HOST}{SELECT_LESSON_API_PATH}"
        select_lesson_data = {
            "action": "list_course",
            "pagenum": pagenum,
            "pagesize": pagesize
        }
        res = requests.get(url=select_lesson_url,params=select_lesson_data,cookies=self.user_cookie)
        return res.json()

if __name__ == '__main__':
    # add_data = get_api_testcase_data("teach_testcase_data.xlsx","增加课程")[0][0]
    # add_res = Teach_Lesson_Manage_Api().add_lesson_api(add_data)
    # print(add_res)
    #
    # change_data = get_api_testcase_data("teach_testcase_data.xlsx", "修改课程")[0][0]
    # change_res = Teach_Lesson_Manage_Api().change_lesson_api(add_res["id"],change_data)
    # print(change_res)

    # delete_res = Teach_Lesson_Manage_Api().delete_lesson_api(add_res["id"])
    # print(delete_res)

    # select_data = Teach_Lesson_Manage_Api().select_lesson_api(1,2)
    # print(select_data)
    data = get_api_testcase_data("teach_testcase_data.xlsx","登录")[0][0]
    res = Teach_Lesson_Manage_Api().teach_login_api(data)
    print(res["retcode"])

