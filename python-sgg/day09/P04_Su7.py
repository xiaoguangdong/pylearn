"""
    通过面向对象的方式实现平川朋友的复杂关系
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__bf = None

    @property
    def bf(self):
        return self.__bf

    @bf.setter
    def bf(self, bf):
        self.__bf = bf

    def __str__(self):
        return f"{self.age}岁的{self.name}带着他的男朋友{self.__bf.name}浪漫的走在宏福科技园"

class BoyFriend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def buy_car(self,car):
        print(f"{self.name}给儿子买了{car.name}一台车")

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color


wf = Student("wf",20)
xb = BoyFriend("wxb",25)
wf.bf = xb
print(str(wf))

su7 = Car("su7","红色")
p1 = Person("xxx",50)
p1.buy_car(su7)






