
"""
    该案例演示了数据类型
"""
# ~~~~~~~~~~~整数类型~~~~~~~~~~~~~~
# 如果数字比较大，可以用下划线优化显示效果，实际输出结果不会发生变化
num1 = 1_000_000_000_000
print(num1)

num3 = 10
num2 = True

# type(参数)  查看参数对应的类型是什么
# isinstance(num1, bool)  判断变量的类型
# type() 不会认为子类是一种父类类型，isinstance() 会认为子类是一种父类类型。
print(num3)
print(num2)
print("~~~~~")

print(type(num1))
print(type(num2))
print(isinstance(num1, int))
print(isinstance(num2, bool))
print(type(num1)==type(num2))
print(f"isinstance(num2, int)->{isinstance(num2, int)}")

# ~~~~~~~~~~~小整数池~~~~~~~~~~~~~~
num5 = 9999
num6 = 9999
# id() 获取变量值在内存中的地址
print(id(num5))
print(id(num6))





# ~~~~~~~~~~~浮点数~~~~~~~~~~~~~~
num10 = 0.1
num11 = 0.2
num12 = num10 + num11
# 注意：在任何的编程语言中，浮点数类型都存在丢失精度的情况
print(num12)  #0.30000000000000004
print(type(num12))

# 为了解决浮点数丢失精度情况，可以借助python其它模块提供的功能
from decimal import Decimal
num13 = Decimal("0.1")
num14 = Decimal("0.2")
num15 = num13 + num14
print(num15)
#
num16 = 3.14e7
print(num16)

# ~~~~~~~~~~~布尔~~~~~~~~~~~~~~
# num1 = True
# num2 = False
# print(num1, num2)
# print(type(num1), type(num2))
#
# # bool是int的子类型，可以和整数进行运算
# print(num1 + 10)
#
# # == 比较运算符   判断==左右两边的值是不是相等
# print(num1 == 1)
# print(num2 == 0)
#
# # is 判断左右两边是否指向内存中的同一个地址
# print(num1 is 1)
# print(num2 is 0)


# ~~~~~~~~~~~字符串~~~~~~~~~~~~~~
# 字符串的表现形式      ''      ""          """   """
# str1 = 'hello'
# str2 = 'world'
# str3 = """wel
#             come"""
# print(str1)
# print(str2)
# print(str3)
#
# str4 = "hell'o w'orld"
# print(str4)


# str1 = "hello\"world"
# print(str1)

# \	在行尾作为续行符
print("hello \
      world")

# \\	反斜杠符号
print("hello \\ world")
# \'	单引号
print("hello \' world")
# \"	双引号
print("hello \" world")
# \b	退格
print("hello\bworld")
# \n	换行
print("hello \n world")
# \t	横向制表符
print("hello \t world")
# \r	回车，回到行首
print("~~~~~~~~~~~~~~~")
print("hello\rwor")


str7 = "hello"
str8 = "hello"
print(id(str7))
print(id(str8))
