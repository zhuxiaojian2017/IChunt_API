#coding:utf-8
import sys,time
# sys.path.append("D:/Mrzhu/IcApi")
sys.path.append("/test/ApiTest/Ichunt_ApiTest/")
from data import login_header
#写入浏览器cookie
login_header.header_write()
#调用登录接口并写入cookie
login_header.login_cookie()
time.sleep(2)
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
# from util.send_email import SendEmail
from util.dd_message import dd_mes
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
    #程序执行的
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        #10  0,1,2,3
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                # expect = self.data.get_expcet_data_for_mysql(i)
                expect = self.data.get_expcet_data(i)
                # sql_data = expect.strip("[]")
                sql_data1 = eval(expect)
                # sql_result = eval(sql_data1)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    #获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                    # print(request_data[depend_key])
                    # res = self.run_method.run_main(method,url,request_data)
                if header == 'write':
                    res = self.run_method.run_main(method,url,request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()

                elif header == 'yes':
                    res = self.run_method.run_main(method,url,request_data)
                    # print(5,res)
                else:
                    res = self.run_method.run_main(method,url,request_data)
                    print(4,res)

                if self.com_util.is_equal_dict(res,sql_data1):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,str(res))
                    fail_count.append(i)
        #将运行结果通过钉钉发送
        dd_mes(pass_count,fail_count)
        exit()

if __name__ == '__main__':
    run = RunTest()

    run.go_on_run()
