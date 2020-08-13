import requests,json
url = "https://www.ichunt.com/v3/login"
url1 = 'https://api.ichunt.com/login/action'
#写入浏览器header信息
def header_write():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    }
    s = requests.session()
    r = s.get(url, headers=headers, verify=False)
    r = s.get(url, headers=headers, verify=False)
    cook = requests.utils.dict_from_cookiejar(s.cookies)
    with open('../data_file/cookie.json', 'w') as f:
        f.write(json.dumps(cook))
        f.close()
#全局请求头部(带header,cookie)
def head():
    with open('../data_file/cookie.json', 'r') as f:
        data = json.load(f)
        PHPSESSID = data['PHPSESSID']
        Yo4teW_gid = data['Yo4teW_gid']
        Yo4teW_csrf = data['Yo4teW_csrf']
        Yo4teW_skey = data['Yo4teW_skey']
        Yo4teW_uid = data['Yo4teW_uid']
        f.close()
    cookies = {
        'cookie': ';'.join([
            'PHPSESSID=%s' % PHPSESSID,
            'Yo4teW_gid=%s' % Yo4teW_gid,
            'Yo4teW_csrf=%s' % Yo4teW_csrf,
            'Yo4teW_skey=%s' %Yo4teW_skey,
            'Yo4teW_uid=%s' %Yo4teW_uid
        ])
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Cookie": cookies['cookie'],
    }
    print(headers)
    return headers

def login_header():
    with open('../data_file/cookie.json','r') as f:
        data = json.load(f)
        PHPSESSID = data['PHPSESSID']
        Yo4teW_gid = data['Yo4teW_gid']
        Yo4teW_csrf = data['Yo4teW_csrf']
        f.close()
    cookies = {
        'cookie': ';'.join([
            'PHPSESSID=%s' % PHPSESSID,
            'Yo4teW_gid=%s' % Yo4teW_gid,
            'Yo4teW_csrf=%s'%Yo4teW_csrf
        ])
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Cookie": cookies['cookie'],
    }
    return headers
#写入登录会员cookie(64650)
def login_cookie():
    with open('../data_file/cookie.json','r') as f:
        data = json.load(f)
    login_param = {
        'account': '13397978821',
        'pwd': '123456',
        'pf': '1'
    }
    r = requests.post(url1,headers=login_header(),data=login_param)
    cook = requests.utils.dict_from_cookiejar(r.cookies)
    for i in cook:
        data[i] = cook[i]
    jsobj = json.dumps(data)
    with open('../data_file/cookie.json', 'w') as f1:
        f1.write(jsobj)
        f1.close()
def post(url, params):
    return requests.post(url, params)

# header_write()
# login_cookie()
head()