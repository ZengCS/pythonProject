print("Python 字典（Dictionary）")
print("字典是一个无序、可变和有索引的集合。在 Python 中，字典用花括号编写，拥有键和值。")
thisdict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
print(thisdict)

# 获取 "model" 键的值：
model = thisdict["model"]
print(f"model is {model}")

# 还有一个名为 get() 的方法会给你相同的结果：
model = thisdict.get("model")
print(f"model is {model}")

# 更改值
# 您可以通过引用其键名来更改特定项的值：
# 把 "year" 改为 2019：
thisdict["year"] = 2019
print(thisdict)

# 遍历字典
# 您可以使用 for 循环遍历字典。
#
# 循环遍历字典时，返回值是字典的键，但也有返回值的方法。
for x in thisdict:  # 等价于:for x in thisdict.keys():
    print(x)

# 逐个打印字典中的所有值：
for x in thisdict:
    print(thisdict[x])

# 您还可以使用 values() 函数返回字典的值：
for x in thisdict.values():
    print(x)

# 通过使用 items() 函数遍历键和值：
for x, y in thisdict.items():
    print(x, y, sep=" --> ")

# 检查键是否存在
# 要确定字典中是否存在指定的键，请使用 in 关键字：
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("No 打叉叉")

# 打印字典中的项目数：
print(f"len is {len(thisdict)}")
print(f"len is {thisdict.__len__()}")

# 添加项目
# 通过使用新的索引键并为其赋值，可以将项目添加到字典中：
thisdict["color"] = "Tiffany blue"
print(thisdict)

# 删除项目
# 有几种方法可以从字典中删除项目：
thisdict.pop("model")
print(thisdict)

# popitem() 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目）：
thisdict.popitem()
print(thisdict)

# del 关键字删除具有指定键名的项目：
del thisdict["year"]
print(thisdict)

# clear() 关键字清空字典：
# 您不能通过键入 dict2 = dict1 来复制字典，因为：dict2 只是对 dict1 的引用，而 dict1 中的更改也将自动在 dict2 中进行。
dict2 = thisdict
copyDict = thisdict.copy()
print(f"dict2 is {dict2}")
thisdict.clear()
print(thisdict)
print(f"dict2 is {dict2}")
# 这里就是面向对象编程
print(f"copyDict is {copyDict}")

# del 关键字也可以完全删除字典：
del thisdict
# print(thisdict) # 删除后不能继续使用，否则报错：NameError: name 'thisdict' is not defined

# 嵌套字典
# 词典也可以包含许多词典，这被称为嵌套词典。
myFamily = {
    "baby": {
        "name": "Star Baby",
        "year": 2018
    },
    "mom": {
        "name": "LX",
        "year": 1991
    },
    "dad": {
        "name": "ZCS",
        "year": 1989
    }
}
print(f"myFamily is {myFamily}")
baby = myFamily.get("baby")

