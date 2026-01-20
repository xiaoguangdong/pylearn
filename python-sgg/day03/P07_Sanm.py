"""
    该案例演示了三目运算符
    表达式1 if 判断条件 else 表达式2
    需求：求2个数中较大的一个
"""
num1 = 10
num2 = 5
# num3 = num1 if num1 > num2 else num2
# print(num3)

if num1 > num2:
    max_num = num1
else:
    max_num = num2

print(max_num)

