import requests,json
from public import login_cookie
class Runmain:

    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)
    def send_get(self,url,data):
        res = login_cookie.logincookie().get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_post(self,url,data):
        res = login_cookie.logincookie().post(url=url,data=data).json()
        # return json.dumps(res,indent=2,sort_keys=True)
        return res

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    Runmain()
    # url = "http://szapi.ichunt.com/public/smsVerify?mobile="
    # data = {
    #     'mobile':'18682159081'
    # }
    # run = Runmain(url+'18682159081','POST',data)
    # print(run.res)