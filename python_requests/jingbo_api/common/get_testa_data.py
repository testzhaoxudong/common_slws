import os
import xlrd


class Get_Api_TestCase_Info:
    def get_excel_testcase_data(self,file_name,sheet_name):
        #定义一个空列表用来存放测试数据
        testcaselist = []
        #获取存放测试用例文档路径
        testcase_path = os.path.join(os.path.dirname(__file__),"..","excel_testcase_data",file_name)
        #使用xlrd方法打开excel文档
        workbook = xlrd.open_workbook(testcase_path)
        #通过sheet页名字来获取sheet页中的测试数据
        sheet_name = workbook.sheet_by_name(sheet_name)
        #获取行数
        maxraws = sheet_name.nrows
        #遍历sheet页中的测试数据（行）
        for row in range(1,maxraws):
            #获取请求参数
            reqinfo = sheet_name.cell(row,8).value
            #获取返回结果并以字典的格式输出，用来做断言
            resinfo = sheet_name.cell(row,10).value
            #获取测试编号
            test_num = sheet_name.cell(row,0).value
            #获取测试标题
            test_title = sheet_name.cell(row,1).value
            #把获取到的测试数据放入到testcaselist中
            testcaselist.append([reqinfo,resinfo,test_num,test_title])
        #返回列表
        return testcaselist
if __name__ == '__main__':
    res = Get_Api_TestCase_Info().get_excel_testcase_data("jb_login_data.xlsx","login")
    print(res[1])






