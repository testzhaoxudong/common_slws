import json
from pprint import pprint

import requests
from python_requests.gkm_api.gkm_common.get_gkm_excel_testcase_data import get_gkm_testcase_data
from python_requests.gkm_api.gkm_config import *
def get_gkm_token():
    get_token_url = f"{HOST}{TOKEN_PATH}"
    data = get_gkm_testcase_data("国康码接口测试用例.xlsx","获取国康码token")[0][0]
    headers = {"Authorization": "Basic a3NwdDpzYWFzX2tzcHQ=",
               "Content-Type": "application/json;charset=UTF-8",
               "Accept": "application/json"}
    res = requests.post(url=get_token_url,params=json.loads(data),headers = headers)
    return res.json()
if __name__ == '__main__':
    pprint(get_gkm_token()["access_token"])
