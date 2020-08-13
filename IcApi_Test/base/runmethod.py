#coding:utf-8
import requests
import json
from data import login_header
heads = login_header.head()
class RunMethod:
    def post_main(self,url,data,header=heads):
        res = None
        if header !=None:           #判断是否带header请求
            print(self,url, header,data)                      #打印post接口请求参数
            res = requests.post(url=url,data=data,headers=heads)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,data=None,header=heads):
        res = None
        if header !=None:
            print(self, url, header, data)                    #打印get接口请求参数
            res = requests.get(url=url,data=data,headers=header,verify=False)
        else:
            res = requests.get(url=url,data=data,verify=False)
        return res.json()

    def run_main(self,method,url,data=None,header=heads):
        res = None
        if method == 'Post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res
        # return json.dumps(res,ensure_ascii=False)
        #return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
