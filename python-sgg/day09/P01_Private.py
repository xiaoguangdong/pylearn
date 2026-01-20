"""
    该案例演示了封装
"""
class Person:
    __home = "earth"

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __eat(self):
        print("eating")

    def eat_1(self):
        print("eating")
        print(self.__home)
        self.__eat()


print(Person._Person__home)

zs = Person("zs",18)
print(zs._Person__name)
