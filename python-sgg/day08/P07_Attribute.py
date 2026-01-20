"""
    该案例演示了属性
"""

class Dog:
    # 类属性
    home = "earth"

    def __init__(self,name,age):
        print("222")
        self.name = name
        self.age = age

# xh = Dog("xh",2)
# print(xh.home)
# print(xh.name)
# print(xh.age)
# xh.color = "baise"
# print(xh.color)
# print("~~~~~~~")
# bg = Dog("bg",3)
# print(bg.home)
# print(bg.name)
# print(bg.age)



#    类属性
print(Dog.home)
wc = Dog()
print(wc.home)

# 通过类名.属性名的方式添加类属性
wc.kemu = "quanke"
# Dog.kemu="quanke"
# Dog.kemu="gouke"

print(wc.kemu)

dh = Dog()
# print(dh.kemu)
# print(Dog.kemu)
print(dh.home)
