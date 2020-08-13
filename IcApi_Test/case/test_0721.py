#coding=utf-8
def test01(a,b):
    if a>b:
        print(a)
        return a
    else:
        print(b)
        return b
test01(10,7)
#三元表达式
def test02(x,y):
    max1 = x if x>y else y
    print(max1)
test02(11,10)

#捕捉异常
def div():
    2/1
try:
    div()
except ZeroDivisionError as e:
    raise ValueError(e)



# bb = aa['data']['list'][0]['order_id']
# print(bb)
