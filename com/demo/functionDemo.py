# Python 函数

print("===== Python 函数 =====")


# 1.函数是一种仅在调用时运行的代码块。
# 2.您可以将数据（称为参数）传递到函数中。
# 3.函数可以把数据作为结果返回。

# 创建函数
# 在 Python 中，使用 def 关键字定义函数：
def my_function():
    print("Hello Function")


# 调用函数
# 如需调用函数，请使用函数名称后跟括号：
my_function()


# 参数
# 信息可以作为参数传递给函数。
# 参数在函数名后的括号内指定。您可以根据需要添加任意数量的参数，只需用逗号分隔即可。
def say_hello(name):
    print(f"Hello {name}")


say_hello("Python")
say_hello("Kotlin")
say_hello("Java")
say_hello("CPP")
say_hello("PHP")
say_hello("World")
say_hello("Kitty")


# 默认参数值
# 下面的例子展示如何使用默认参数值。
# 如果我们调用了不带参数的函数，则使用默认值：
def my_country(country="China"):
    print("I am from " + country)


my_country()
my_country("Sweden")
my_country("England")
my_country("USA")


def find_fruit(fruits, position=0):
    msg = "the No.{} Fruit is {}"
    print(msg.format(position, fruits[position]))


fruits = ["apple", "banana", "cherry"]


def getLastPosition():
    return len(fruits) - 1


find_fruit(fruits)
find_fruit(fruits, position=1)
find_fruit(fruits, getLastPosition())


def math_square(x):
    return x ** 2


print(math_square(3))
print(math_square(5))
print(math_square(9))


# 任意参数
# 如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
# 这样，函数将接收一个参数元组，并可以相应地访问各项：
def youngest_child(*kids):
    print("The youngest child is " + kids[2])


youngest_child("Phoebe", "Jennifer", "Rory")


# 递归
# Python 也接受函数递归，这意味着定义的函数能够调用自身。
# 递归是一种常见的数学和编程概念。它意味着函数调用自身。这样做的好处是可以循环访问数据以达成结果。
# 开发人员应该非常小心递归，因为它可以很容易地编写一个永不终止的，或者使用过量内存或处理器能力的函数。但是，在被正确编写后，递归可能是一种非常有效且数学上优雅的编程方法。
#
# 例子：使用递归打印99乘法表
def calc99Tab(row, col):
    if row > 1:
        if col > 1:
            calc99Tab(row, col - 1)
        else:
            calc99Tab(row - 1, row - 1)
    result = row * col
    if result < 10:
        # 增加空格输出，使表格对齐
        msg = " {}x{}={}"
    else:
        msg = "{}x{}={}"
    print(msg.format(col, row, result), end="  ")
    if col == row:
        print("")


# 打印99乘法表
calc99Tab(9, 9)
