"""
异常关机断电警报接口
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/getPowerAlarm"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": "322205109",
    "startTime": "2021-06-28 22:16:56"
        }
result = requests.post(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)