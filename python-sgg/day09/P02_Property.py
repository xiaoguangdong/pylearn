"""
    该案例演示了封装相关的注解
"""
"""
# @property  将方法转换为属性
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(f"{self.name} eats!")


zsf = Person("zsf")

# 默认情况下，当调用实例方法的时候，必须 对象.方法名(),哪怕没有参数，括号也不能省略
# zsf.eat()

# 如果在方法上加了@property注解(将方法转换为属性)，那么在调用实例方法的时候，直接通过对象.方法名   后面的括号不用加
zsf.eat
"""
# 通过@property注解实现只读属性
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @property
    def name(self):
        if self.__name == "zsf":
            print("换个名字")
            self.__name = "zwj"
        return self.__name

    @name.setter
    def name(self, name):
        if name == "ssss":
            name = "aaaa"
        self.__name = name

zsf = Person("zsf")
# 私有化属性不能直接在类的外部进行访问
# print(zsf.__name)

# 可以提供专门的方法对私有属性进行访问，将结果返回给调用者
# print(zsf.name)

# zsf.name = "ssss"
# print(zsf.name)



