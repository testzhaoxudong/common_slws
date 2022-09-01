import csv
import os

class  Get_Test_Info:
    #定义一个函数用来获取测试配置信息
    def get_test_config(self,file_name,key):
        #获取保存配置数据的路径
        config_path = os.path.join(os.path.dirname(__file__),"..","..","config",file_name)
        #打开获取的文件并且赋予阅读权限，重命名为info
        with open(config_path,"r",encoding="utf-8") as info:
            #使用csv读取文件
            csv_info = csv.reader(info)
            #以字典的格式输出并返回
            dict_info = dict(csv_info)[key]
            return dict_info

    def get_test_data(self,file_name,line):
        data_path = os.path.join(os.path.dirname(__file__),"..","..","data",file_name)
        with open(data_path,"r",encoding="utf-8") as info:
            csv_info = csv.reader(info)
            list_info = list(csv_info)[line]
            return list_info

    #定义一个函数用来获取测试配置信息
    def get_test_database_config(self,file_name):
        #获取保存配置数据的路径
        config_path = os.path.join(os.path.dirname(__file__),"..","..","config",file_name)
        #打开获取的文件并且赋予阅读权限，重命名为info
        with open(config_path,"r",encoding="utf-8") as info:
            #使用csv读取文件
            csv_info = csv.reader(info)
            #以字典的格式输出并返回
            dict_info = dict(csv_info)
            return dict_info


if __name__ == '__main__':
    # config = Get_Test_Info().get_test_config("dp_url.csv","dp_pc_url")
    # print(config)
    data = Get_Test_Info().get_test_data("out_jingjia_data",1)
    print(data)
    # db = Get_Test_Info().get_test_database_config("db_122_112_251_17.csv")
    # print(db)