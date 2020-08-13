import time
import json
from data import login_header
url2 = 'https://szapi.ichunt.com/msg/sendMessageByAuto?'
def dd_mes(pass_list,fail_list):
    def md5(data):
        import hashlib
        hash = hashlib.md5()
        hash.update(str(data).encode(encoding='utf-8'))
        return hash.hexdigest()

    timestamp = int(time.time())
    pass_num = float(len(pass_list))
    fail_num = float(len(fail_list))
    count_num = pass_num + fail_num

    pass_result = "%.2f%%" % (pass_num / count_num * 100)
    fail_result = "%.2f%%" % (fail_num / count_num * 100)
    message_param = {
        'k1': timestamp,
        'k2': md5(md5(timestamp) + 'fh6y5t4rr351d2c3bryi'),
        'pf': 1,
        'keyword': 'zgj-dd-task',
        'touser': json.dumps(['18682159081']),
        'data': json.dumps({'total': count_num, 'suc': pass_num, 'fail': fail_num, 'percent': pass_result, 'fail_percent': fail_result},
                           ensure_ascii=False),
        'wechat_data': '',
        'is_ignore': ''
    }
    req = login_header.post(url2, params=message_param)
    result = req.json()

# dd_mes("12","34")