
"""
    该案例演示了self
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

    def study(self):
        print("studying")

    def eat_study(self):
        # 在实例方法中调用其他的实例方法
        self.eat() # Student.eat(self)
        self.study()


zsf = Student("zsf",81)
zsf.eat_study()

