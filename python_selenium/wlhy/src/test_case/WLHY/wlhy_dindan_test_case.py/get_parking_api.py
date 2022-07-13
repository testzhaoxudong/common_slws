"""
获取停车点接口
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/getParkingPoint"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": "322205109",
    #"searchDate": "2021-06-28 11:43:01",
    "startTime": "2021-06-28 11:43:01",
    "endTime": "2021-06-28 11:43:01",
    "resident": 50,
    "speed": "",
    "isSave": "是"
}
result = requests.get(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)