"""
车辆列表接口
"""
import requests as requests
from requests import request
URL = "http://119.3.43.36:8900/gpsApi/carlist"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "tenantId": 764537,
    "version": 1,
    "endTime": "2021-11-01 10:24:56",
    "startTime": "2021-11-23 10:24:56"
}
result = requests.post(url=URL,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)