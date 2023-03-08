import json
import requests

from python_requests.gkm_api.gkm_common.get_gkm_excel_testcase_data import get_gkm_testcase_data
from python_requests.gkm_api.gkm_common.gkm_get_token_api import get_gkm_token
from python_requests.gkm_api.gkm_config import *
class GkmManage:
    gkm_token = get_gkm_token()["access_token"]
    def get_gkm_token(self):
        get_token_url = f"{HOST}{TOKEN_PATH}"
        data = get_gkm_testcase_data("国康码接口测试用例.xlsx", "获取国康码token")[0][0]
        headers = {"Authorization": "Basic a3NwdDpzYWFzX2tzcHQ=",
                   "Content-Type": "application/json;charset=UTF-8",
                   "Accept": "application/json"}
        res = requests.post(url=get_token_url, params=json.loads(data), headers=headers)
        return res.json()
    def get_gkm_info(self,cardNumber,userName):
        get_info_url = f"{HOST}{GKM_PATH}"
        data = {"cardNumber":cardNumber,
                "userName": userName}
        headers = {"Blade-Auth":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ0ZW5hbnRfbmFtZSI6bnVsbCwidXNlcl9uYW1lIjoiaGVhbHRoX2NvZGVfYWNjZXNzX3Rva2VuX2FkbWluIiwidXNlcl9mcmVlemVfZmxhZyI6IjAiLCJhdmF0YXIiOiIiLCJhdXRob3JpdGllcyI6WyJhZG1pbiJdLCJjbGllbnRfaWQiOiJrc3B0IiwiZGF0YV9zb3VyY2UiOm51bGwsInJvbGVfbmFtZSI6ImFkbWluIiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwidXNlcl90eXBlIjpudWxsLCJjb21wYW55bm8iOm51bGwsInVzZXJfaWQiOiIxNDcxNDIyNzY0NzIwMjIwNzI4Iiwicm9sZV9pZCI6IjIwMjAxMTEzMTc1MzAxIiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IuiOt-WPlumJtOadg-eUqOaIt--8jOS4jeWPr-WIoOmZpCIsImNsaWVudCI6bnVsbCwiZXhwIjoxNjY2ODcxNjYxLCJkZXB0X2lkIjoiMTE2OTUyNjMyMDI0NjM4NjY5MCIsImp0aSI6IjA4ODBjOTU5LTMyODUtNDI5NC04MDdiLWJjZmYzZTUyZmE2YyIsImFjY291bnQiOiJoZWFsdGhfY29kZV9hY2Nlc3NfdG9rZW5fYWRtaW4ifQ._U2yWjpXrVWaI20WXeEPXsV9kuplXxUqfBxb7nzQ7Eo",
                   "Authorization": "Basica3NwdF9kcml2ZXI6c2Fhc19rc3B0X2RyaXZlcg==",
                   "access_token":self.gkm_token}
        res = requests.post(url=get_info_url, params=data, headers=headers)
        return res.json()


if __name__ == '__main__':
    # token = GkmManage().get_gkm_token()
    # print(token["access_token"])
    info = GkmManage().get_gkm_info(622429199801243137,"赵旭东")
    print(info)