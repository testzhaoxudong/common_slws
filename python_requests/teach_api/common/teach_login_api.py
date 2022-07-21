from pprint import pprint

import requests
from python_requests.teach_api.teach_config import *
def teach_ligin():
    teach_login_url =  f"{HOST}{LOGIN_API_PATH}"
    teach_login_data = {
        "username": "auto",
        "password": "sdfsdfsdf"
    }
    res = requests.post(url=teach_login_url,data=teach_login_data)
    return res.cookies,res.json(),res.status_code
if __name__ == '__main__':
    pprint(teach_ligin())
