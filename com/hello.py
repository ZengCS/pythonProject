# 第一个注释
# 第二个注释
from com.demo import main

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""


# function
def test():
    print("Row-1 in test()")
    print("Row-2 in test()")


print("Hello Python3")
test()

print('----------')
# 条件控制
condition: bool = True
if condition:
    print("True")
else:
    print("False")

print('----------')
# 数组
print("数组List")
_list = ['item_one', 2, 'item_three', 4.0, 'item_five']
_list[0] = "item_1"  # 修改第一个item的值
print(f"the array is {_list}")
print(f"the first is {_list[0]}")
print(f"从第二个开始输出到第三个元素{_list[1:3]}")  # 从第二个开始输出到第三个元素
print(f"输出从第三个元素开始的所有元素{_list[2:]}")  # 输出从第三个元素开始的所有元素

print('----------')

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
print('元组Tuple')
_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinyTuple = (123, 'runoob')

print(_tuple)  # 输出完整元组
print(_tuple[0])  # 输出元组的第一个元素
print(_tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(_tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinyTuple * 2)  # 输出两次元组
print(_tuple + tinyTuple)  # 连接元组
print('----------')
# 数字(Number)类型
i: int = 1
f: float = 2.0
bo: bool = False
# print(f"xxx={xxx}") f=format 格式化,xxx=变量名
print(f"i = {i}")
print(f"f = {f}")
print(f"b = {bo}")

# 字符串(String)
# python中单引号和双引号使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，


什么都没有


可以由多行组成"""

print(f"word is {word}")
print(f"sentence is {sentence}")
print(f"paragraph is {paragraph}")

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '-你好')  # 连接字符串
print(f'{str}-你好')  # 连接字符串，与上面等价

print('----------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('----------')
# 不换行输出
print(x, end=",")
print(y, end=",")
print("c")

a = b = c = 1
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print('----------')
a, b, c = 1, 2.3, "runoob"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# 标准数据类型 Python3 中有六个标准的数据类型：
#
# Number（数字）String（字符串）List（列表）Tuple（元组）Set（集合）Dictionary（字典）
#
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(f"复数：d={d}")
print(f"实数：d.real={d.real}")
print(f"虚数：d.imag={d.imag}")
# 运算
print(5 + 4)  # 加法
print(4.3 - 2)  # 减法
print(3 * 7)  # 乘法
print(2 / 4)  # 除法，得到一个浮点数
print(2 // 4)  # 除法，得到一个整数
print(17 % 3)  # 取余
print(2 ** 10)  # 乘方

main.reverseWords("I like runoob")

# set
print("----- Set -----")
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
print("----- set集合运算 -----")
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素
