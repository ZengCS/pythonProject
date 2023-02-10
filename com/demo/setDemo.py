print("Python 集合（Set）")
print("集合是无序和无索引的集合。在 Python 中，集合用花括号编写。")
# 创建集合，使用{}
thisset = {"apple", "apple", "apple", "banana", "cherry"}
print(thisset)
# 注释：集合是无序的，因此您无法确定项目的显示顺序。
# 注释：集合内元素不可重复，出现重复将自动去重。

# 访问项目
# 您无法通过引用索引来访问 set 中的项目，因为 set 是无序的，项目没有索引。
# 但是您可以使用 for 循环遍历 set 项目，或者使用 in 关键字查询集合中是否存在指定值。
for x in thisset:
    print(f"x = {x}")
if "banana" in thisset:
    print("Yes,banana in the set")
else:
    print("No,打叉叉")

# 更改项目
# 集合一旦创建，您就无法更改项目，但是您可以添加新项目。

# 添加项目
# 要将一个项添加到集合，请使用 add() 方法。
# 要向集合中添加多个项目，请使用 update() 方法。
thisset.add("orange")
print(thisset)

thisset.update(["orange", "mango", "grapes"])
print(thisset)

# 获取 Set 的长度
# 要确定集合中有多少项，请使用 len() 方法。
print(f"len is {len(thisset)}")
print(f"len is {thisset.__len__()}")

# 删除项目
# 要删除集合中的项目，请使用 remove() 或 discard() 方法。
# 注释：如果要删除的项目不存在，则 remove() 将引发错误。
thisset.remove("banana")
print(thisset)

# 使用 discard() 方法来删除 “banana”：
# 注释：如果要删除的项目不存在，则 discard() 不会引发错误。
thisset.discard("banana")
print(thisset)

# 您还可以使用 pop() 方法删除项目，但此方法将删除最后一项。请记住，set 是无序的，因此您不会知道被删除的是什么项目。
# pop() 方法的返回值是被删除的项目。
x = thisset.pop()
print(f"the 倒霉蛋 is {x}")
print(thisset)

# clear() 方法清空集合：
thisset.clear()
print(thisset)

# del 彻底删除集合：
del thisset
# NameError: name 'thisset' is not defined
# print(thisset)

# 合并两个集合
# 在 Python 中，有几种方法可以连接两个或多个集合。
# 您可以使用 union() 方法返回包含两个集合中所有项目的新集合，也可以使用 update() 方法将一个集合中的所有项目插入另一个集合中：

# union() 方法返回一个新集合，其中包含两个集合中的所有项目：
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3}
print(f"set2 ={set2}")

set3 = set1.union(set2)
print(f"set3 ={set3}")

# update() 方法将 set2 中的项目插入 set1 中：
set1.update(set2)
print(f"set1 ={set1}")

# 注释：union() 和 update() 都将排除任何重复项。

# 返回为两个其他集合的交集的集合。
# 取并集
set4 = set1.intersection(set2)
print(f"intersection = {set4}")
