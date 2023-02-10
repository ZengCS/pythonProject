class MyClass:
    x = 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("My Name is {},I am {} years old".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)  # 也可以用Person.__init__()，不推荐
        self.year = year

    def say_hello(self):
        print("My Name is {},I am {} years old,I will graduation at {}".format(self.name, self.age, self.year))
