
"""
    该案例演示了python的输出
"""
#~~~~~~~1.普通输出~~~~~~~~~
# print("hello world")
# print("hello" + "world" + "welcome")
# name = input("输入名")
# print("您输入的姓名是:" + name)
# print("您输入的姓名是:" , name)

# print("hello world",end="\n")
# print("hello world",end="")
# print("abc")
#~~~~~~~2.格式化输出~~~~~~~~~
# （1）字符串中使用 % 占位
num1 = 10.1
num2 = 3.14
str1 = "num1= %d,num2= %.3f " % (num1,num2)
print(str1)

# num1 = 10
# num2 = 3.14
num3 = False
# （2）字符串.format()----不设置指定位置，按默认顺序
str = "num1={},num2={},num3={}".format(num1, num2, num3)
print(str)
# （2）字符串.format()----设置指定位置，不能和方式1混合使用
# str = "num1={0},num2={2},num3={1}".format(num1, num3,num2)

# （2）字符串.format()----设置参数
str = "num1={n1},num2={n2},num3={n3}".format(n1 = num1, n3 = num3, n2 = num2)
print(str)
# （3）数字格式化：
float1 = 31415.9
str2 = "{:*^20,.2f}".format(float1)
str3 = "{:*<20,.2f}".format(float1)
str4 = "{:*>20,.2f}".format(float1)
print(str2)  # *****31,415.90******
print(str3)  # *****31,415.90******
print(str4)  # *****31,415.90******
# # （4）使用大括号 {} 来转义大括号
# print ("{0} 对应的位置是 {0}".format("hello"))
# print ("{} 对应的位置是 {{0}}".format("hello"))
# （5）f-字符串
num1 = 10
num2 = 3.14
# str1 = "num1={},num2={}".format(num1, num2)
# str1 = f"num1={num1},num2={num2}"

#要求：指定名字必须得相同
str1 = f"{num1=},{num2=}"
print(str1)
