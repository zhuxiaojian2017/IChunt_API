#coding:utf-8
import json
class OperetionJson:

    def __init__(self,file_path=None):
        if file_path  == None:
            # self.file_path = '/var/lib/jenkins/workspace/Ichunt_ApiTest/data_file/user.json'
            self.file_path = '../data_file/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]

    #写json
    def write_data(self,data):
        # with open('/var/lib/jenkins/workspace/Ichunt_ApiTest/data_file/cookie.json', 'w') as fp:
        with open('../data_file/cookie.json','w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
    opjson = OperetionJson()
    print(opjson.get_data('cookie'))
    # op_json = OperetionJson('../data_file/cookie.json')
    # a = op_json.read_data()
    # b = a['User-Agent']
    # print(b)
