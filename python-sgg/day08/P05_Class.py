"""
    该案例演示了类的定义以及访问类中成员
"""
class Person:
    """这是一个人的类"""
    home = "home"
    def __init__(self):
        self.age = 0

    def eat(self):
        print("eating")

    def drink(self):
        print("drink")


# 引用
print(Person.home)
print(Person.eat)
print(Person.drink)
print(Person.__doc__)

# 实例化
zsf = Person()
print(zsf.home)
# Person.eat()
zsf.eat() #==>Person.eat(zsf)
zsf.drink()



