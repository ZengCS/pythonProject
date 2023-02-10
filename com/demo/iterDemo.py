# Python 迭代器
print("===== Python 迭代器 =====")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

x = 100
y = 100

print(x, y)


def myfunc():
    global x

    x = 200
    y = 200
    print(x, y)


myfunc()

print(x, y)
