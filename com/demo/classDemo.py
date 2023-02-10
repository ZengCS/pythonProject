import platform

import myModule as mx
from com.bean.EntitySet import MyClass, Person, Student

obj = MyClass()
print("obj.x = {}".format(obj.x))

p1 = Person("Bill", 63)
print(p1.name)
print(p1.age)

p1.name = "Thomson"
p1.age = 18
p1.say_hello()

stu = Student("Mick", 12, 2022)
stu.say_hello()

mx.greeting("Jackson")

print(platform.system())
print(platform.version())
print(platform.machine())
print(platform.release())
print(platform.mac_ver())
x = dir(platform)
print(x)
dirs = dir(stu)
for p in dirs:
    if p.startswith("_"):
        continue
    print(p, end=", ")
