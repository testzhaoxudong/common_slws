import json
import os
import xlrd


def get_api_testcase_data(file_name,sheet_name):
    #定义一个空列表用来存放excel中读取的测试数据
    testcaselist = []
    #获取存放测试用例的文档路径
    testcase_path = os.path.join(os.path.dirname(__file__),"..","excel_api_testcase_data",file_name)
    #使用xlrd三方库打开文档
    workbook = xlrd.open_workbook(testcase_path)
    #通过打开的文档获取sheet页名称
    worksheet = workbook.sheet_by_name(sheet_name)
    #获取sheet页中的有效行数
    maxrows = worksheet.nrows
    #遍历
    for row in range(1,maxrows):
        #获取请求参数
        reqinfo = worksheet.cell(row,8).value
        # 获取请求返回结果
        resinfo = json.loads( worksheet.cell(row,10).value)
        #获取测试用例编号
        testcase_num = worksheet.cell(row,0).value
        #获取测试用例标题
        testcast_title = worksheet.cell(row,2).value
        #将获取到的测试数据存放在列表中
        testcaselist.append([reqinfo,resinfo,testcase_num,testcast_title])
    return testcaselist

if __name__ == '__main__':
    res = get_api_testcase_data("teach_testcase_data.xlsx","登录")
    print(res)

