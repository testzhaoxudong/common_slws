# list1 = ['西西','边边','a1', '马', 'TY','清心']
# #  列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
# # 方法1： 手动扩充--字典--存放在列表里面；{}
# # 方法2： 自动--dict（）--不强制 list.appen()
# # list2 =
# dict1 = {"西西":['西西','男','18','济南'],"边边":['边边','男','18','山东']}
# list2 = [dict1]
# print(list2)
# list2["key"] = input("name：")
# for dict1["key"] in list1:
#     if dict1["key"] == "西西":
#         print(dict1["西西"])
#     elif dict1["key"] == "边边":
#         print(dict1["边边"])











# 案例2：获取dictory里的信息，并且把url的value值， data中嵌套字典的每个value值，按行输出
import json

dictory={'url':'http://www.baidu.com','data':{'username':'admin','pwd':'123456'}}
for i in dictory:
    print(dictory[i])
    if i == 'data':
        for j in dictory[i].values():
            print(type(dictory[i]))
            print(dictory[i])
# print(type(dictory))
# a = dictory["url"]
# print(dictory["url"])
# print(type(a))




# print(dictory['url'].values())
# a = dict(dictory['url'])
# print(type(dictory["url"]))
# print(dictory.items())










