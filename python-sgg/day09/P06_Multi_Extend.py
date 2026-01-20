"""
    该案例演示了多继承
"""
class Person:
    """人的类"""

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")

class YellowRace(Person):
    """黄种人，继承人类"""
    color = "yellow"

    def run(self):
        print("run...yel")

class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("study...")

    def run(self):
        print("run...stu")

class ChineseStudent(YellowRace,Student):
    country = "china"

zsf = ChineseStudent("zsf",80)
print(zsf.country)
print(zsf.color)
print(zsf.home)
zsf.study()
zsf.run()
zsf.eat()



