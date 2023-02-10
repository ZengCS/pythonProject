a = 30
b = 60
c = 80
if a > b:
    print("a>b")
elif a > c:
    print("a>c")
else:
    print("a is min")

if c > a and c > b:
    print("c is max")
else:
    print("c is not max")

if b > c or b > a:
    print("b is not min")
else:
    print("b is min")

# if 语句不能为空，但是如果您处于某种原因写了无内容的 if 语句，请使用 pass 语句来避免错误。
if a < b:
    pass

print("the end")
