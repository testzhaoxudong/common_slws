"""
查询待维修车辆记录
"""
import requests

url = "http://119.3.43.36:8900/gpsApi/getUnRepairedDeviceFaultRecords"
headers = {
    "Content-Type": "application/json"
            }
data = {
    "deviceId": "322205109",
    "carNumber": "皖SB6867",
    "companyId": "",
    "startTime": "2021-06-28 11:43:01",
    "endTime": "2021-06-28 11:43:01",
    "tenantId": "764537"
}
result = requests.post(url=url,headers=headers,json=data)
print(r"请求响应结果为：",result.text)
print(r"请求的状态代码为：",result.status_code)