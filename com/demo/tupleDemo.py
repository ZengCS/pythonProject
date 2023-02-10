# 元组
print("元组")
# 创建元组：
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)

# 您可以通过引用方括号内的索引号来访问元组项目：
print(thistuple[0])

# 负索引
# 负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目，依此类推。
print(thistuple[-1])

# 索引范围
# 您可以通过指定范围的起点和终点来指定索引范围。
# 指定范围后，返回值将是带有指定项目的新元组。
# 注释：搜索将从索引 2（包括）开始，到索引 5（不包括）结束。
print(thistuple[2:5])

# 负索引范围
# 如果要从元组的末尾开始搜索，请指定负索引：
print(thistuple[-3:-1])

# 更改元组值
# 创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。
# 但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组。
thislist = list(thistuple)
thislist.append("gigi")
thislist[4] = "猕猴桃"
thistuple = tuple(thislist)
print(thistuple)

# 遍历元组
# 您可以使用 for 循环遍历元组项目。
for name in thistuple:
    print(f"fruit is {name}")

# 检查项目是否存在
# 要确定元组中是否存在指定的项，请使用 in 关键字：
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No,打叉叉")

# 元组长度
# 要确定元组有多少项，请使用 len() 方法：
print(f"len is {len(thistuple)}")
print(f"len is {thistuple.__len__()}")

# 创建有一个项目的元组
# 如需创建仅包含一个项目的元组，您必须在该项目后添加一个逗号，否则 Python 无法将变量识别为元组。
singleTuple = ("apple",)
print(type(singleTuple))

# 不是元组
notSingleTuple = ("apple")
print(type(notSingleTuple))
# 等价于
notSingleTuple = "apple"
print(type(notSingleTuple))

# 删除项目
# 注释：您无法删除元组中的项目。
# 元组是不可更改的，因此您无法从中删除项目，但您可以完全删除元组：
del thistuple

# 删除后，将不能在使用，否则程序会报错
# print(thistuple) # 这会引发错误，因为元组已不存在。

# 合并两个元组
# 如需连接两个或多个元组，您可以使用 + 运算符：
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = tuple(("apple", "banana", "cherry"))  # 请注意双括号
print(thistuple)
# 统计元组中共有几个apple
print(thistuple.count("apple"))
# 找到apple的位置
print(thistuple.index("apple"))
