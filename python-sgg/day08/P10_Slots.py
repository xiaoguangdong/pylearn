"""
    该案例演示了限制实例的属性和方法
"""
import types


class Person:
  __slots__ = ("name", "age", "eat")

  def __init__(self, name=None):
    self.name = name




def eat(self):
  print(f"{self.name}在吃饭")


def drink(self):
  print(f"{self.name}在喝水")


p = Person("张三")

# 添加实例属性
p.age = 10
print(p.age)  # 10

# 添加实例属性
# p.weight = 100  # AttributeError: 'Person' object has no attribute 'weight'
# print(p.weight)


# 添加实例方法
# p.eat = types.MethodType(eat, p)
# p.eat()  # 张三在吃饭


# 添加实例方法
p.drink = types.MethodType(drink, p)  # AttributeError: type object 'type' has no attribute 'MethodType'
