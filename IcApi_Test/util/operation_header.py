# coding:utf-8
import requests
import json
from util.operation_json import OperetionJson
from data import login_header
header = login_header.head()

class OperationHeader:
    # def __init__(self, response):
    #     self.response = json.loads(response)

    # def get_response_url(self):
    #     '''
    #     获取登录返回的token的url
    #     '''
    #     url = self.response
    #     return url

    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        # url = self.get_response_url() + 'jQuery18302987472692348341_1541384774644'
        cookie = requests.get(url).cookies
        print("------------------")
        print(cookie,type(cookie))
        return cookie

    def write_cookie(self):
        # cookie_sessid = requests.utils.dict_from_cookiejar(self.get_cookie())
        # ichunt_cookie = requests.utils.dict_from_cookiejar(res.cookies)
        # cookie = dict(cookie_sessid,**ichunt_cookie)
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        op_json = OperetionJson()
        op_json.write_data(cookie)


if __name__ == '__main__':
    url = "https://api.ichunt.com/login/action"
    data = {
        "account": "18682159081",
        "pwd": "654321",
        "pf": "1"
    }
    res = header.post(url,data)
    # res = json.dumps(header.post(url, data).json())
    op_header = OperationHeader()
    op_header.write_cookie()
