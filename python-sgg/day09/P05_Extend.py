"""
    该案例演示了继承
"""
class Person:
    """人的类"""
    # 类属性
    home = "earth"

    def __init__(self, name):
        #实例属性
        self.name = name

    def eat(self):
        print("eating")

class YellowRace(Person):
    color = "yellow"

class WhiteRace(Person):
    color = "white"

class BlackRace(Person):
    color = "black"

zsf = YellowRace("zsf")
print(zsf.color)
print(zsf.home)

zsf.eat()



