"""
设备状态接口
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/getDevicestatus"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": "322205109"
        }
result = requests.post(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)


