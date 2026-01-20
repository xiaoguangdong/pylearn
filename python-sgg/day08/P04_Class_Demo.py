"""
    该案例演示了简单的类的定义以及对象的创建
"""

# 定义一个学生类
class Student:
    '''这是一个学生类'''
    # 类属性   所有类的实例共享的
    school = "atguigu"

    # 在创建学生对象（实例）的时候，会自动调用的方法
    def __init__(self, name, age):
        # 定义实例属性   每个实例属性是独立的，相互不影响
        self.name = name
        self.age = age

    # 实例方法  方法第一个参数是self，表示当前实例对象
    # 对象.方法() 调用当前方法的时候，会将当前对象自身作为参数传递给方法
    def play_game(self):
        print(f"{self.age}岁的{self.name}正在专注的玩着游戏")

    def study(self):
        print(f"{self.age}岁的{self.name}正在有一搭没一搭的学着")

    def video(self):
        print(f"{self.age}岁的{self.name}正在录着视频")

# 通过类这个模板创建当前类的实例(对象)
mzl = Student("mzl",23)
print(mzl.name)
print(mzl.age)
print(mzl.school)
mzl.video()

dgd = Student("dgd", 23)
print(dgd.name)
print(dgd.age)
print(mzl.school)
dgd.study()


