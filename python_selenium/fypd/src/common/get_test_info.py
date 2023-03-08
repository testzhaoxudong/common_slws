import csv
import os
class GetTestInfo:
    #获取测试数据
    def get_test_data(self,file_name,line):
        testdata_path = os.path.join(os.path.dirname(__file__),"..","..","data",file_name)
        with open(testdata_path,"r",encoding="utf-8") as data:
            reader_data = csv.reader(data)
            list_data = list(reader_data)[line]
        return list_data


    #获取配置信息
    def get_test_config(self,file_name,key):
        testdata_config = os.path.join(os.path.dirname(__file__),"..","..","config",file_name)
        with open(testdata_config,"r",encoding="utf-8") as data:
            reader_data = csv.reader(data)
            dict_data = dict(reader_data)
        return dict_data[key]

if __name__ == '__main__':
    data = GetTestInfo().get_test_data("login_test_case_data.csv",1)
    print(type(data))
    print(data)
    config = GetTestInfo().get_test_config("slws_url.csv","pc_url")
    print(config)

