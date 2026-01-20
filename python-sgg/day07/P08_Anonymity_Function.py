"""
    该案例演示了匿名函数
"""
from functools import reduce

"""
# 需求：完成一个实现两个数+、-、*、/简单计算的计算器
def ope1(num1,num2):
    return num1 + num2

def ope2(num1,num2):
    return num1 - num2

def ope3(num1,num2):
    return num1 * num2

def ope4(num1,num2):
    return num1 / num2

# 定义一个计算函数，接收参与运算的两个数，并调用相关的运算方法去进行计算
def cal(num1,num2,op):
    return op(num1,num2)


print(cal(20, 10, ope1))
print(cal(20, 10, ope2))
print(cal(20, 10, ope3))
print(cal(20, 10, ope4))
"""
"""
# 定义一个计算函数，接收参与运算的两个数，并调用相关的运算方法去进行计算
def cal(num1,num2,op):
    return op(num1,num2)


print(cal(20, 10, lambda a,b: a + b))
print(cal(20, 10, lambda a,b: a - b))
print(cal(20, 10, lambda a,b: a * b))
print(cal(20, 10, lambda a,b: a / b))
"""
"""
# 有三名学生的姓名和年龄，按年龄排序。
student_list = [{"name": "zhang3", "age": 36},
                {"name": "li4", "age": 14},
                {"name": "wang5", "age": 27}]

# def getKey(std):
#     return std["age"]
# student_list.sort(key= getKey)
student_list.sort(key= lambda stu: stu["age"])
print(student_list)
"""
"""
# map() 函数对序列中元素逐一处理。
list1 = [0, 1, 3, 7, 9]
print(list(map(lambda item: item * item, list1)))
"""
"""
# filter() 函数对序列中元素过滤。
list1 = [-0, -1, -3, 7, 9]
print(list(filter(lambda item: item > 0, list1)))
"""
# reduce() 函数对序列中元素进行累积。
list1 = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, list1))
