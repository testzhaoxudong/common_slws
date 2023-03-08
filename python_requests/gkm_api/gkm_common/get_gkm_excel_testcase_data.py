import json
import os

import xlrd


def get_gkm_testcase_data(file_name,sheet_name):
    # 新建一个列表用于存放测试数据
    testcaselist = []
    # 获取测试用例文档存放路径
    get_gkm_excel_testcase_data_path = os.path.join(os.path.dirname(__file__),"..","gkm_excel_api_testcase_data",file_name)
    # 使用三方库xlrd打开excel文档
    workbook = xlrd.open_workbook(get_gkm_excel_testcase_data_path)
    # 获取excel文档sheet也名称
    worksheet = workbook.sheet_by_name(sheet_name)
    # 获取sheet页中的测试数据有效行数
    max_nrows = worksheet.nrows
    # 遍历：获取有效的测试数据
    for data in range(1,max_nrows):
        # 获取请求参数
        reqinfo = worksheet.cell(data,8).value
        # 获取请求返回结果，用于断言
        resinfo = json.loads(worksheet.cell(data,10).value)
        # 获取测试用例编号
        testcase_num = worksheet.cell(data,0).value
        # 获取测试用例标题
        testcase_title = worksheet.cell(data,2)
        testcaselist.append([reqinfo,resinfo,testcase_num,testcase_title])
    return testcaselist
if __name__ == '__main__':
    data = get_gkm_testcase_data("国康码接口测试用例.xlsx","国康码查询接口测试用例")
    print(data)


