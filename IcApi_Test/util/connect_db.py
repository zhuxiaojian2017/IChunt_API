import pymysql
import json
# def get_data(sql):
#     conn = None
#     try:
#         conn= pymysql.connect(host='192.168.1.232',
#                               port = 3306,
#                               user='root',
#                               passwd='123456',
#                               db ='test',
#                               charset='utf8')       #这里不加上charset='utf-8'中文会显示??
#
#         cur = conn.cursor()
#         cur.execute(sql)
#         data = cur.fetchall()
#         result = []
#         for row in data:
#             result.append(row)
#         return result
#     except Exception as e:
#         print(e)
#     finally:
#         if conn and cur:
#             cur.close()
#             conn.close()
#
# sql = 'SELECT Case_id,locationMode,locationValue,testdata from test_data_1'

import json
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.1.232',
            port=3306,
            user='root',
            passwd='123456',
            db='api',
            charset='utf8',
            )
        self.cur = self.conn.cursor()

    #查询一条数据
    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result, ensure_ascii=False)
        return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select result from Account_Api where CaseID=1")
    print(res)
    # sss = res.strip("[]")
    # print(sss)
    # rey = eval(sss)
    # print(rey,type(rey))
    # sssdd = eval(rey)
    # print(sssdd)
    # print(type(sssdd))
    # print(sssdd['err_code'])