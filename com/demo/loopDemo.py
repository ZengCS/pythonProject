# Python循环
# 1.While循环
# 如果使用 while 循环，只要条件为真，我们就可以执行一组语句。
i = 1
while i < 7:
    print(i, end=",")
    i += 1
print("while end")
# 注释：请记得递增 i，否则循环会永远继续。

# break 语句
# 如果使用 break 语句，即使 while 条件为真，我们也可以停止循环：
i = 1
while i < 7:
    print(i, end=",")
    if i == 3:
        break  # 结束循环并跳出
    i += 1
print("\nbreak end")

# continue 语句
# 如果使用 continue 语句，我们可以停止当前的迭代，并继续下一个：
i = 0
while i < 7:
    i += 1
    if i == 3:
        continue  # 结束本次循环，进入下一次循环
    print(i, end=",")
print("\ncontinue end")

# else 语句
# 通过使用 else 语句，当条件不再成立时，我们可以运行一次代码块：
i = 1
while i < 6:
    print(i, end=",")
    i += 1
else:
    print("\ni is no longer less than 6")

print("while else end")

# 2.For循环
# Python For 循环
# for 循环用于迭代序列（即列表，元组，字典，集合或字符串）。
# 这与其他编程语言中的 for 关键字不太相似，而是更像其他面向对象编程语言中的迭代器方法。
# 通过使用 for 循环，我们可以为列表、元组、集合中的每个项目等执行一组语句。

print("\n----------For 循环")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x, end=" ")
print("\n--------------------")
for x in range(10):
    print(x, end=",")
# 注意：range(10) 不是 0 到 10 的值，而是值 0 到 9。
# range() 函数默认 0 为起始值，不过可以通过添加参数来指定起始值：range(3, 10)，这意味着值为 3 到 10（但不包括 10）：
print("\n--------------------")
for x in range(3, 10):
    print(x, end=",")
print("\n--------------------")
# range() 函数默认将序列递增 1，但是可以通过添加第三个参数来指定增量值：range(2, 30, 3)：
start = 3  # 起点,包含
stop = 50  # 终点,不包含
step = 6  # 步长,每次递增的值,默认为1
for x in range(start, stop, step):
    print(x, end=",")
print("\n--------------------")

# 打印 0 到 9 的所有数字，并在循环结束时打印一条消息：
for x in range(10):
    print(x, end=",")
else:
    print("Finally finished!")
print("--------------------")

# 嵌套循环
# 嵌套循环是循环内的循环。
# “外循环”每迭代一次，“内循环”将执行一次：
adj = ["红", "大", "甜"]
fruits = ["苹果", "香蕉🍌", "草莓🍓"]

for x in adj:
    for y in fruits:
        print(x, y)
