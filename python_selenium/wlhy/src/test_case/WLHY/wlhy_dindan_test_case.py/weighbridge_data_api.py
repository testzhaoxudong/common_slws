"""
地磅数据上传接口
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/upWeight"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "carNumber": "苏AF6185",
    "time": "2021-06-01 11:30:01",
    "weight": 200,
    "factoryId": "26130",
    "factoryName": "",
    "deviceId": "",
    "taskId": "",
    "version": "",
}
result = requests.post(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)
