import csv
import os


class GetYkjtTestInfo:
    # 分装一个函数用来获取测试数据
    def get_test_data(self,fiel_name,line):
        # 获取测试数据的路径
        data_path = os.path.join(os.path.dirname(__file__),"..","..","data",fiel_name)
        # 读取测试数据并打开赋予阅读权限
        with open(data_path,"r",encoding="utf-8") as data:
            reader_csv = csv.reader(data)
            data_list = list(reader_csv)
            return data_list[line]

    def get_test_config(self,file_name,key):
        config_path = os.path.join(os.path.dirname(__file__),"..","..","config",file_name)
        with open(config_path,"r",encoding="utf-8") as config:
            resder_csv = csv.reader(config)
            config_dict = dict(resder_csv)
            return config_dict[key]
    def get_test_database(self,file_name):
        url_path = os.path.join(os.path.dirname(__file__),"..","..","config",file_name)
        with open(url_path,"r",encoding="utf8") as file_data:
            file_value = csv.reader(file_data)
            dict_file = dict(file_value)
            return dict_file

if __name__ == '__main__':
    data = GetYkjtTestInfo().get_test_data("ykjt_login_data.csv",3)
    print(data)
    config = GetYkjtTestInfo().get_test_config("ykjt_url.csv","ykjt_url")
    print(config)
    db = GetYkjtTestInfo().get_test_database("47.97.212.214.csv")
    print(db)