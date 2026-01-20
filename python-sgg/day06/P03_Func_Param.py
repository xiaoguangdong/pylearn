"""
    该案例演示了函数的参数
    需求：先打印2*3的*，在打印1*6的*
"""
"""
# 不抽取函数
num = 2
while num >0:
    print("*" * 3)
    num -= 1
print("~"*30)
num = 1
while num >0:
    print("*" * 6)
    num -= 1
"""
"""
# 抽取函数
def print_star_1():
    num = 2
    while num > 0:
        print("*" * 3)
        num -= 1

def print_star_2():
    num = 1
    while num > 0:
        print("*" * 6)
        num -= 1

print_star_1()
print("~"*30)
print_star_2()
"""
# 抽取函数（加参数）---向控制台打印*
def print_star(rows,cols):
    while rows > 0:
        print("*" * cols)
        rows -= 1


print_star(2,300)
print("~"*30)
print_star(1,6)

