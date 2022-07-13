import csv
import os


class GetTestInfo():
    def get_test_info(self,file_name):
        url_path = os.path.join(os.path.dirname(__file__),"..","..","config",file_name)
        with open(url_path,"r",encoding="utf8") as file_data:
            file_value = csv.reader(file_data)
            dict_file = dict(file_value)
        return dict_file
    def get_test_data(self,file_name,line):
        url_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", file_name)
        with open(url_path, "r", encoding="utf8") as file_data:
            file_value = csv.reader(file_data)
            list_file = list(file_value)[line]
            return list_file

if __name__ == '__main__':
    a = GetTestInfo().get_test_data("wlhy_add_carrier_data.csv",1)
    print(a)