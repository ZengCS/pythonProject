import datetime
import time
import json

# 2021-12-20 15:48:41.241503

x = datetime.datetime.now()
print(x)
print(type(x))
print(x.year)
print(type(x.tzinfo))
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17, 12, 0, 0)
print(x)

timestap = int(time.time() * 1000)
print("时间戳(ms)：{}".format(timestap))
# 把时间戳转换成日期
dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(dateTime)
dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestap / 1000))
print(dateTime)

# 一些 JSON:
x = '{ "name":"Bill", "age":63, "city":"Seatle"}'

# 解析 x:
y = json.loads(x)

# 结果是 Python 字典：
print(y["age"])


def fun1():
    a = 5  # 自动转成int
    print(type(a))
    a = 5.5  # 自动转成float
    print(type(a))
    a = "halo"  # 自动转成str
    print(type(a))


fun1()

str = "我是字符串"
i = 1  # 整数
f = 1.0  # 普通浮点数
b = True  # 布尔值


def showMsg(msg):
    print("msg = " + msg)


showMsg("Hello Python")

# 我是列表
mList = ["A", "B", "C", "B", "A"]
for letter in mList:
    print("letter is " + letter)

# 我是元组
mTuple = ("A", "B", "C", "B", "A")
# 我是集合
mSet = {"A", "B", "C", "B", "A"}
# 我是词典(我感觉我是JSON)
mDictionary = {
    "java": {
        "name": "高斯林",
        "year": 1995
    },
    "python": {
        "name": "吉多·范罗苏姆",
        "year": 1990
    }
}
# usage
print(mDictionary.get("java").get("name"))

a = 200
b = 66
if a > b:
    print("a > b")
elif a == b:
    print("a = b")
else:
    print("a < b")

a += 1
