"""
    该案例演示了多态
"""

class Bird:
    def __init__(self, name):
        self.name = name

class Fish:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self, flag):
        ani = None
        match flag:
            case '1':
                ani = Bird("红火")
            case '2':
                ani = Fish("小鱼儿")
            case '3':
                ani = Dog("wangc")
        return ani

    def feed(self,ani):
        print(f"{self.name}正在悉心的喂养他的小动物{ani.name}")


wf = Person("wf",20)
# ani = wf.call('3')
# print(ani.name)
y1 = Fish("小鱼儿")
d1 = Dog("ahuang")
b1 = Bird("飞飞")
wf.feed(y1)
wf.feed(d1)
wf.feed(b1)