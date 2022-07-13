"""
设备待维修列表接口
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/getRepairedList"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": "322205109",
    "startTime": "2019-05-20 00:00:01"
        }
result = requests.post(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)