## api自动化测试框架

## 文件目录说明
1. base 基础包,目前只封装了runmethod,给post/get
2. case 用例目录,暂时没用
3. data 数据封装层
 3.1. data_config:定义excel不同列属性值及封装函数
 3.2 dependent_data:执行依赖测试并返回结果
 3.3 get_data:获取excel数据
 3.4 login_header:请求浏览器并保存cookie文件
4. main 运行主函数  run_test.py
5. util 工具包
 5.1 comcom_util:三种断言方式封装
 5.2 connect_db：db库连接函数封装,暂时没用
 5.3 dd_message:钉钉消息发送
 5.4 operation_excel:excel操作函数封装
 5.5 operation_header:heaer读取及写入封装，暂时没用
 5.6 operation_json:接口json文件读取及写入封装
 5.7 send_email:邮件发送函数封装

