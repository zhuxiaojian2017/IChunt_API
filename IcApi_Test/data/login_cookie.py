import requests
import unittest
from data import login_header
header = login_header.head()
# login = login_header.login_cookie()
class Login_phone(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.ichunt.com/v3/login"
        self.url1 = 'https://api.ichunt.com/login/action'
        self.url2 = "https://api.ichunt.com/order/create"
    def test01_get_phone_null(self):
        '''手机号为空'''
        login_param = {
            'account' : '18682159081',
            'pwd' : '123456',
            'pf' : '1'
        }
        req = requests.post(self.url1,headers=header,params=login_param)
        cook = requests.get(self.url1).cookies
        print(cook)
        cookies = requests.utils.dict_from_cookiejar(req.cookies)
        print(cookies)
        result = req.json()
        print(result)
        # self.assertEqual(result['err_code'],11001)
        # self.assertEqual(result['err_msg'],'请输入手机号/邮箱/企业登录名')
    def test02_order_create(self):
        # headers = {
        #     header,
        # }
        login_param = {
            'pf':'1',
            'pay_type':'1',
            'shipping_type':'1',
            'tax_id':'0',
            'address_id':'596',
            'user_coupon_id':'-1',
            'cart_id':'3348'
        }
        # cookies = {
        #     'Yo4teW_skey=%s' % login['Yo4teW_skey'],
        #     # 'PHPSESSID=%s' % cookie_sessid,
        #     'Yo4teW_uid=%s' % login['Yo4teW_uid'],
        #     # 'Yo4teW_csrf=%s' % cookie_csrf,
        # }
        # cookiejar = login.session().cookies
        req = requests.post(self.url2,headers=header,params=login_param)
        print(header)
        print(req.json())
    def tearDown(self):
        print("over")

if __name__ == '__main__':
    unittest.main()