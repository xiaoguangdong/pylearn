"""
    该案例演示了方法
"""
import types


def drink(self):
    print("drinking")

class Student:
    """这是一个学生类"""
    school = "atguigu"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print(self.school)
        print(self.name)
        print(self.age)

    # 类方法
    @classmethod
    def get_info(cls):
        print(cls.school)
        print(cls.__doc__)

zwj = Student("zwj",30)
# zwj.eat()
# zwj.get_info()
# Student.get_info()

# zwj.drink = drink
# zwj.drink()

# Student.drink = drink
# zwj.drink()
# Student.drink(zwj)

zcs = Student("zcs",50)

zcs.drink = types.MethodType(drink, zcs)
zcs.drink()


class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b


print(MathUtil.add(10, 20))
