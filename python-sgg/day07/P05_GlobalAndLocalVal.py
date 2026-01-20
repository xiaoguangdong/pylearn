"""
    该案例演示全局变量和局部变量
    全局作用域下定义的变量-全局变量--作用于整个模块
    局部作用域下定义的变量-局部变量--作用于当前函数
"""
sum = 0  # 这是一个全局变量

def add(num1,num2) :
    sum = num1 + num2  # 这是一个局部变量
    print("函数内局部变量的值:",sum,id(sum))
    # return sum

add(10,20)
# print(num1) # num1访问不到
print("函数外全局变量:",sum,id(sum))
