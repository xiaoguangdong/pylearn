"""
    该案例演示了函数的抽取
"""
# 定义了一个函数，功能是向控制台打印2*3的*
def print_star():
    num = 2
    while num > 0:
        print("*" * 3)
        num -= 1


# 通过函数名去调用函数
print_star()
print("~"*30)
print_star()
