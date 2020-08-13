#coding:utf-8
import json
import operator
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否再另外一个字符串中
        str_one:查找的字符串
        str_two：被查找的字符串
        '''
        flag = None
        # if isinstance(str_one):
        # 	str_one = str_one.encode('unicode-escape').decode('string_escape')
        # return operator.eq(str_one,str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_str(self,str_one,str_two):
        flag = None
        if str_one == str_two:
            flag = True
        else:
            flag = False
        return flag


    def is_equal_dict(self,dict_one,dict_two):
        '''
        判断两个字典是否相等
        '''
        flag = None
        # if dict_one['err_code'] == dict_two['err_code'] and dict_one['err_msg'] == dict_two['err_msg']:
        #     flag = True
        # # elif dict_one['error_code'] == dict_two['error_code'] and dict_one['error_msg'] == dict_two['error_msg']:
        # #     flag = True
        # else:
        #     flag = False
        # return flag
        if 'err_code' in dict_one.keys():
            if dict_one['err_code'] == dict_two['err_code'] and dict_one['err_msg'] == dict_two['err_msg']:
                flag = True
            else:
                flag = False
        elif 'error_code' in dict_one.keys():
            if dict_one['error_code'] == dict_two['error_code'] and dict_one['error_msg'] == dict_two['error_msg']:
                flag = True
            else:
                flag = False
        elif 'errcode' in dict_one.keys():
            if dict_one['errcode'] == dict_two['errcode'] and dict_one['errmsg'] == dict_two['errmsg']:
                flag = True
            else:
                flag = False
        else:
            flag = False
        return flag

        # if isinstance(dict_one,str):
        #     dict_one = json.loads(dict_one)
        #     # print(dict_one)
        # if isinstance(dict_two,str):
        #     dict_two = json.loads(dict_two)
        #     # print(dict_two)
        # return operator.eq(dict_one,dict_two)