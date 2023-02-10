import random

print("Hello World!")


# 方法注释1
# 方法注释2
# 方法注释3
def fun1():
    a = 5  # 自动转成int
    b = 3.2  # 自动转成float
    print(f"{a} + {b} = {a + b}")
    print(f"type(a) = {type(a)}")
    a = 5.5
    print(f"type(a) = {type(a)}")


def fun2():
    msg: str = "Hello fun2"  # 自动转成str
    # msg: str = "Hello fun2"
    print(msg)


fun1()
fun2()

# Python 允许您在一行中为多个变量赋值：
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 您可以在一行中为多个变量分配相同的值：
x = y = z = "Orange"
print(x)
print(y)
print(z)


def myFun():
    x = "Apple"  # IDE 发出警告:name 'x' from outer scope
    print(f"x = {x}")


myFun()
print(f"x = {x}")


# 通常，在函数内部创建变量时，该变量是局部变量，只能在该函数内部使用。
# 要在函数内部创建全局变量，您可以使用 global 关键字。
def myFun2():
    global g
    g = "fantastic"


myFun2()

print(f"Python is {g}")

# 内置数据类型
# 文本类型：	str
# 数值类型：	int, float, complex
# 序列类型：	list, tuple, range
# 映射类型：	dict
# 集合类型：	set, frozenset
# 布尔类型：	bool
# 二进制类型：	bytes, bytearray, memoryview

# 您可以使用 type() 函数获取任何对象的数据类型：
x = 10
print(type(x))

x = range(6)
print(x)

x = 10  # int
y = 6.8  # float
z = 1j  # complex

# 把整数转换为浮点数
a = float(x)

# 把浮点数转换为整数 - 去尾法，不会四舍五入
b = int(y)

# 把整数转换为复数：
c = complex(x)

# 注：您无法将复数转换为其他数字类型。
# 复数只能分开操作 实部和虚部

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# 随机整数[1,10)
print(random.randrange(1, 10))

# 随机整数，步长2，表示只有偶数, 只会返回[0,2,4,6,8]
print(random.randrange(0, 10, 2))

# 随机浮点数[0.0,1.0)
print(random.random())

# int() float() str()
x = str("S2")  # x 将是 'S2'
y = str(3)  # y 将是 '3'
z = str(4.0)  # z 将是 '4.0'

print(x)
print(y)
print(z)

a = """
Python is a widely used general-purpose, high level programming language. 

It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 

It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code.
"""
print(a)

# 字符串是数组
a = "Hello, World!"
print(a)
# len() 函数返回字符串的长度：
print(len(a))
print(a[0])
print(a[0:5])  # 从0到4,不包括5
print(a[7:12])
print(a[-6:-1])

# strip() 方法删除开头和结尾的空白字符（类似Java trim）
a = "  Hello, World!        "
a = a.strip()
print(a)  # returns "Hello, World!"

# lower() 返回小写的字符串：
print(a.lower())

# upper() 方法返回大写的字符串：
print(a.upper())

# replace() 用另一段字符串来替换字符串：
print(a.replace("World", "Kitty"))  # 把World 替换 成Kitty

# split() 方法在找到分隔符的实例时将字符串拆分为子字符串：
print(a.split(","))  # returns ['Hello', ' World!']

# 检查以下文本中是否存在短语 "ina"：
txt = "China is a great country"
x = "ina" in txt
print(x)

# 正如在 Python 变量一章中所学到的，我们不能像这样组合字符串和数字：
# 这段代码会报错 TypeError: can only concatenate str (not "int") to str
#
# age = 63
# txt = "My name is Bill, I am " + age
# print(txt)

# 但是我们可以使用 format() 方法组合字符串和数字！
# {} 的数量必须<=format(*args)的参数数量
age = 63
txt = "My name is Bill, and I am {},{}"
print(txt.format(age, age ** 2, 2))

# 您可以使用索引号 {0} 来确保参数被放在正确的占位符中：
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# 非0 都是True 或者非空
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool(()))
print(bool([]))
print(bool({}))

print(bool("Hello"))
print(bool(10))

print(type(x))
if isinstance(x, int):
    print("x is int")
else:
    print("x is not int")

# for 循环
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# 如需确定列表中有多少项，请使用 len() 方法：
print(thislist.__len__())
print(len(thislist))

# 如需将项目添加到列表的末尾，请使用 append() 方法：
thislist.append("orange")
print(thislist)

# 要在指定的索引处添加项目，请使用 insert() 方法：
thislist.insert(0, "grape")
print(thislist)

# remove() 方法删除指定的项目：
thislist.remove("banana")
print(thislist)

# pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）：
thislist.pop()
thislist.pop(1)
print(f"pop {thislist}")

# del 关键字删除指定的索引：
del thislist[0]
print(thislist)

# clear() 方法清空列表：
thislist.clear()
print(thislist)

# del 关键字也能完整地删除列表：
del thislist
# 此时再使用就会报错：NameError: name 'thislist' is not defined
# print(thislist)

list1 = ["c", "a", "d"]
list2 = [3, 1, 2]
list1.sort()  # 正序 得到 acd
list2.sort(reverse=True)  # 反序 得到 321
list2.reverse()  # 翻转 得到123
list3 = list1 + list2

print(list3)
