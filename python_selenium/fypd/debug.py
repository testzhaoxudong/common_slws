
#get_test_info
from python_selenium.fypd.src.common.get_test_info import GetTestInfo
if __name__ == '__main__':
    data = GetTestInfo().get_test_data("login_test_case_data.csv",1)
    print(data)
    config = GetTestInfo().get_test_config("url.csv","pc_url")
    print(config)