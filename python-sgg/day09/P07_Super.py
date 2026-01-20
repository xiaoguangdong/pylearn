"""
    该案例演示了复用父类中的属性或者方法
"""
class Person:
    home = "earth"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} eating")

class YellowPerson(Person):
    color = "yellow"

    def run(self):
        print(f"{self.name} runs")

class Student(Person):

    def __init__(self,name,age,grade):
        # 调用父类中的方法  方式1：通过super().父类方法名
        super().__init__(name,age)
        self.grade = grade

    def study(self):
        print(f"{self.name} studying")

class ChineseStudent( YellowPerson,Student):
    country = "China"

    def xuexi(self):
        # 先吃饱
        super().eat()
        # 调用父类中的方法  方式1：通过父类名.父类方法名(self)
        # Person.eat(self)
        # 再锻炼好
        super().run()
        # 再学习
        super().study()
        print(super().home)

zwj = ChineseStudent("zwj",20,"一年级")

print(zwj.name)
print(zwj.age)
print(zwj.grade)
zwj.xuexi()
print("~~~"*30)
print(ChineseStudent.__mro__)
