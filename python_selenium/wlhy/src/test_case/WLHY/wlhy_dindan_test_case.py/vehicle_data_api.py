"""
车辆实时数据接口
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/realtime"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": 322205109,
    "lastData": 0,
    "version": 1,
}
result = requests.get(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)
