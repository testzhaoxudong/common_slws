"""
历史数据接口[多种返回类型]

"""
import requests

url = "http://119.3.43.36:8900/gpsApi/dataCenter"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": "322205109",
    "startTime": "2021-06-01 11:30:01",
    "endTime": "2021-06-30  11:30:01",
    "status": "0",
    "isSave": "1"
}
result = requests.post(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)
