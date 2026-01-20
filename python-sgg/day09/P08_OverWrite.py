"""
    该案例演示了方法的重写
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("父类中的eat方法")

class ChineseStudent(Student):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade = grade

    # def eat(self):
    #     print(f"{self.name}用筷子吃饭")

zwj = ChineseStudent("zwj",20,"一年级")
zwj.eat()


